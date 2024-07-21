from pydantic import BaseModel

class ProductSchema(BaseModel):
    title: str
    price: str
    image_url: str
    path_to_image: str
    
    class Config:
        from_attributes = True
    
    def to_json(self):
        return {
            "title":self.title,
            "price":self.price,
            "image_url":self.image_url,
            "path_to_image": self.path_to_image,
        }
