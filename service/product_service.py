from models.models import Product

class ProductService():
    def __init__(self,db) -> None:
        self.db = db

    def get_product(self):
        result = self.db.query(Product).all()
        return result
        
    def create_product(self,product:Product):
        new_product = Product(
            name = product.name,
            brand = product.brand,
            description = product.description,
            price = product.price,
            entry_date = product.entry_date,
            availability = product.availability,
            available_quantity = product.available_quantity
        )
        self.db.add(new_product)
        self.db.commit()
        return
    
    def get_for_id(self, id:int):
        result = self.db.query(Product).filter(Product.id == id).first()
        return result
    
    def update_product(self,data:Product):
        product = self.db.query(Product).filter(Product.id == data.id).first()
        product.name = data.name
        product.brand = data.brand
        product.description = data.description
        product.price = data.price
        product.entry_date = data.entry_date
        product.availability = data.availability
        product.available_quantity = data.available_quantity
        self.db.commit()
        return
    
    def delete_product(self, id:int):
        self.db.query(Product).filter(Product.id == id).delete()
        self.db.commit()