import datetime
from typing import Optional
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    id: Optional[int]=None
    name : str = Field(max_length=40, min_length=2,description="product name")
    brand : str = Field(max_length=30, min_length=2,description="name of product brand")
    description : str =Field(max_length=100, min_length=8,description="product description")
    price : float = Field(ge=100)
    entry_date : datetime.date = Field(description="product delivery date")
    availability : bool = Field (description="product availability")
    available_quantity : int = Field (ge=1, le=10000000)

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                'name':'vive100',
                'brand':'vive100',
                'description':'exquisito producto para recargarte el dia',
                'price':2000,
                'entry_date':'2023-05-29',
                'availability':True, 
                'available_quantity':1000
            }
        }