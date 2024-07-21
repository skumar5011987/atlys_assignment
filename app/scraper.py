import requests
from bs4 import BeautifulSoup
import os
from tenacity import retry, stop_after_attempt, wait_fixed
from .models import Product
from .schemas import ProductSchema
from .config import settings
from .cache import *

class Scraper:
    def __init__(self, page_limit=settings.page_limit, proxy=settings.proxy, cookies=settings.cookies):
        self.page_limit = page_limit
        self.proxy = proxy
        self.cookies = cookies
        self.base_url = 'https://dentalstall.com/shop/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.proxies = {
            'http': proxy,
            'https': proxy
        } if proxy else None
        self.products = []


    @retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
    def fetch_page(self, page_num):
        url = f"{self.base_url}page/{page_num}/"
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxies, cookies=self.cookies)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            return None
        
    def fetch_product(self, url=""):
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxies, cookies=self.cookies)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching product {url}: {e}")
            return 'N/A'
        
    def scrape(self):
        for page_num in range(1, self.page_limit + 1):
            html = self.fetch_page(page_num)
            if html:
                self.parse_page(html)

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        product_cards = soup.select('.product')
        for card in product_cards:
            
            product_title = card.find('div', class_='mf-product-content').find('h2').get_text()
            price_str = card.find('span', class_='woocommerce-Price-amount amount').get_text()
            image_url = card.find('div', class_='mf-product-thumbnail').find('img', class_='attachment-woocommerce_thumbnail size-woocommerce_thumbnail')['data-lazy-src'].strip()
            
            # product_url = card.find('div', class_='mf-product-thumbnail').find('a').get('href')
            # product_title, price_str, image_url = self.get_product_details(product_url) # this can be used to get product's comlete details by opening product card
            
            path_to_image = self.download_image(image_url)
            self.products.append(ProductSchema(title=product_title, price=price_str, image_url=image_url, path_to_image=path_to_image))
            

    # Method to open product cards and scrape product's complete info
    def get_product_details(self, url=''):
        if not url:
            return ""
                
        html = self.fetch_product(url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('div', class_='entry-left').find('h1').text.strip()
        price = soup.find('span', class_='woocommerce-Price-amount amount').get_text()
        image_url = soup.find('div', class_='woocommerce-product-gallery__image').find('img').get('src','').strip()
        return title, price, image_url
        
    def download_image(self, url):
        response = requests.get(url, stream=True)
        file_name = url.split("/")[-1]
        file_path = os.path.join("images", file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_path

    def save_products(self, products):
        Product.save_to_db(products)

    def load_existing_products(self):
        return get_all_cached_products()
