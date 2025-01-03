from sqlalchemy import Float, String, Column,Integer,Boolean,Date,ForeignKey
from db.config import Base

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key =True)
    name = Column(String)
    brand = Column(String)
    description = Column(String)
    price = Column(Float)
    entry_date = Column(Date)
    availability = Column(Boolean)
    available_quantity = Column(Integer)

class Supplier(Base):
    __tablename__ = "supplier"
    id = Column(Integer,primary_key=True)
    sub_name = Column(String)
    address = Column(String)
    phone = Column(Integer)
    email = Column(String) 

class Supplies(Base):
    __tablename__ ="supplies"
    id = Column(Integer, primary_key = True)
    product_id = Column(Integer, ForeignKey("product.id"))
    supplier_id = Column(Integer, ForeignKey("supplier.id"))
    purchase_price = Column(Float)