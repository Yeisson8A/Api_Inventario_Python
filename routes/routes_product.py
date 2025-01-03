from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from db.config import Session
from schemas.product_schema import ProductSchema
from service.product_service import ProductService
from logger.logger import logger

product_router = APIRouter()

@product_router.get('/product',tags=['product'],status_code=200)
def get_product():
    logger.info(f"service: '/product', method: 'GET")
    db = Session()
    result = ProductService(db).get_product()
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@product_router.get('/product_for_id',tags=['product'],status_code=200)
def get_product_for_id(id:int):
    logger.info(f"ID: {id}, service: '/product_for_id', method: 'GET")
    db = Session()
    result = ProductService(db).get_for_id(id)
    return JSONResponse (content=jsonable_encoder(result), status_code=200)

@product_router.post('/product',tags=['product'],status_code=201)
def create_product(product:ProductSchema):
    logger.info(f"Datos: {jsonable_encoder(product)}, service: '/product', method: 'POST")
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse (content={"message": "product created succesfully", "status_code": 201}, status_code= 201)

@product_router.put('/product{id}', tags=['product'])
def update_product(id: int, data: ProductSchema):
    logger.info(f"Datos: {jsonable_encoder(data)}, service: '/product', method: 'PUT")
    db = Session()
    result = ProductService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "Product not found", "status_code": 404})
    ProductService(db).update_product(data)
    return JSONResponse(content={"message": "Product updated successfully", "status_code": 200}, status_code=200)

@product_router.delete('/product{id}',tags=['product'])
def delete_product(id:int):
    logger.info(f"ID: {id}, service: '/product', method: 'DELETE")
    db = Session()
    result = ProductService(db).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"product don't found", "status_code":404})
    ProductService(db).delete_product(id)
    return JSONResponse(content={"message":"product deleted succesfully", "status_code":200}, status_code=200)