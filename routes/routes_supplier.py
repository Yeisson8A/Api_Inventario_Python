from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from db.config import Session
from schemas.supplier_schema import SupplierSchema
from service.supplier_service import SupplierService
from logger.logger import logger

supplier_router = APIRouter()

@supplier_router.get('/supplier', tags = ['supplier'], status_code=200)
def get_supplier():
    logger.info(f"service: '/supplier', method: 'GET")
    db = Session()
    result = SupplierService(db).get_supplier()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplier_router.get('/supplier_for_id', tags = ['supplier'], status_code=200)
def get_supplier_for_id(id:int):
    logger.info(f"ID: {id}, service: '/supplier_for_id', method: 'GET")
    db = Session()
    result = SupplierService(db).get_for_id_supplier(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplier_router.post('/supplier', tags=['supplier'], status_code= 200)
def create_supplier(supplier:SupplierSchema):
    logger.info(f"Datos: {jsonable_encoder(supplier)}, service: '/supplier', method: 'POST")
    db = Session()
    SupplierService(db).create_supplier(supplier)
    return JSONResponse(content={"message":"supplier created", 'status_code': 200})


@supplier_router.put('/supplier{id}', tags=['supplier'])
def update_supplier(id:int,data:SupplierSchema):
    logger.info(f"Datos: {jsonable_encoder(data)}, service: '/supplier', method: 'PUT")
    db = Session()
    result = SupplierService(db).get_for_id_supplier(id)
    if not result:
        return JSONResponse(content= {"message":"supplier don't found", "status_code":400})
    SupplierService(db).update_supplier(id,data)
    return JSONResponse(content={"message":"supplier update", "status_code":200}, status_code= 200)

@supplier_router.delete('/supplier{id}',tags=['supplier'])
def delete_supplier(id:int):
    logger.info(f"ID: {id}, service: '/supplier', method: 'DELETE")
    db = Session()
    result = SupplierService(db).get_for_id_supplier(id)
    if not result:
        return JSONResponse(content= {"message":"supplier don't found", "status_code": 404})
    SupplierService(db).delete_supplier(id)
    return JSONResponse(content={"message":"supplier deleted succesfully", "status_code": 200}, status_code=200)