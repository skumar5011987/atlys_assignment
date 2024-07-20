from fastapi import FastAPI, BackgroundTasks, Depends, Query
from sqlalchemy.orm import Session
from .auth import verify_token
from .scraper import Scraper
from .models import Product
from .schemas import ProductSchema
from .database import init_db, get_db
from .cache import *

app = FastAPI()

def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message": f"Welcome to Atlys, Lets starts!!"}

def run_scraping(page_limit: int, proxy: str, cookies: dict):
    scraper = Scraper(page_limit=page_limit, proxy=proxy, cookies=cookies)
    existing_products = scraper.load_existing_products()
    scraper.scrape()

    new_products = []
    for product in scraper.products:
        if not any(p.get('price') == product.price for p in existing_products):
            new_products.append(product)
    
    if new_products:
        scraper.save_products(new_products)
        set_products_to_cache(new_products)
    
    print(f"Scraped products:{len(scraper.products)}, New products:{len(new_products)} Saved producs:{len(new_products)}.")

@app.post("/scrape")
def scrape_products(background_tasks: BackgroundTasks, token: str = Depends(verify_token), page_limit: int = Query(5, alias="page_limit"), proxy: str = "", cookies: dict = {}):
    background_tasks.add_task(run_scraping, page_limit, proxy, cookies)
    return {"message": "Scraping started in background..."}

@app.get("/products", response_model=dict)
def get_products(db: Session = Depends(get_db), token: str = Depends(verify_token)):
    products = Product.get_from_db()
    data={
        "status": "ok",
        "count": len(products),
        "results":[product.dict() for product in products]
    }
    return data

@app.post("/clear_cache")
def clear_cache(db: Session = Depends(get_db), token: str = Depends(verify_token)):
    clear_cache_products()
    return {"message": "Ok"}
