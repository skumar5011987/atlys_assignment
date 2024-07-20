import json
from .schemas import ProductSchema
from .database import SessionLocal, ProductModel

class Product:
    def __init__(self, title: str, price: float, image_url: str):
        self.title = title
        self.price = price
        self.image_url = image_url

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "image_url": self.image_url
        }

    @staticmethod
    def save_to_file(products, file_path="products.json"):
        with open(file_path, 'w') as f:
            json.dump([product.to_dict() for product in products], f)

    @staticmethod
    def load_from_file(file_path="products.json"):
        try:
            with open(file_path, 'r') as f:
                products_data = json.load(f)
                return [Product(**data) for data in products_data]
        except FileNotFoundError:
            return []
    
    @staticmethod
    def get_from_db():
    
        db = SessionLocal()
        try:
            products = db.query(ProductModel).all()
            return [ProductSchema(
                title=product.title,
                price=product.price,
                image_url=product.image_url
            ) for product in products]
        except Exception as e:
            print(e)
        finally:
            db.close()

    @staticmethod
    def save_to_db(products):
        db = SessionLocal()
        try:
            for p in products:
                existing_product = db.query(ProductModel).filter_by(title=p.title).first()
                if existing_product:
                    existing_product.title = p.title
                    existing_product.price = p.price
                    existing_product.image_url = p.image_url
                else:
                    product = ProductModel(title=p.title, price=p.price, image_url=p.image_url)
                    db.add(product)
                db.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            db.close()
