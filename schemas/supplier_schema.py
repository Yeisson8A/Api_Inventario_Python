from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class SupplierSchema (BaseModel):
    id : Optional[int]
    sub_name : str = Field(max_length=40,min_length=2,description="name supplier")
    address : str = Field(max_length=40,min_length=2,description="fitting room address")
    phone : int = Field(ge=5)
    email : EmailStr = Field(max_length=40,min_length=2,description="provider email")
    
    class config:
        schemas_extra = {
            "example":{
                "id":1,
                "sub_name":"colanta",
                "address":"cualquiera",
                "phone":3158000000,
                "email":"example@gmail.com"            
            }
        }