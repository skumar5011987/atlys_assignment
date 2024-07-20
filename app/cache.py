import redis
import json
from .models import Product

# Initialize connection
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def clear_cache_products():
    keys = redis_client.keys('*')
    for key in keys:
        if key.endswith('.jpg'):
            redis_client.delete(key)
def get_cached_product(image_url):
    cached_data = redis_client.get(image_url)
    if cached_data:
        return json.loads(cached_data)
    return None

def get_all_cached_products():
    keys = redis_client.keys('*')
    products = []
    for key in keys:
        if key.endswith('.jpg'):
            product_data = redis_client.get(key)
            if product_data:
                products.append(json.loads(product_data))
    
    # if not products:
    #     products = Product.get_from_db()
    #     set_products_to_cache(products)
    return products

def set_products_to_cache(products):
    for p in products:
        cache_product(p)

def cache_product(product):
    image_url = product.image_url
    try:
        redis_client.set(image_url, json.dumps(product.to_json()), ex=60*24*60*60)
    except Exception as e:
        print(e)
