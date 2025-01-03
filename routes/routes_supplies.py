from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from db.config import Session
from schemas.supplies_schema import SuppliesSchema
from service.supplies_service import SuppliesService
from logger.logger import logger

supplies_router = APIRouter()

@supplies_router.get('/supplies', tags = ['supplies'], status_code=200)
def get_supplies():
    logger.info(f"service: '/supplies', method: 'GET")
    db = Session()
    result = SuppliesService(db).get_supplies()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplies_router.get('/supplies_for_id', tags = ['supplies'], status_code=200)
def get_supplies_for_id(id:int):
    logger.info(f"ID: {id}, service: '/supplies_for_id', method: 'GET")
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplies_router.post('/supplies', tags=['supplies'], status_code= 200)
def create_supplies(supplies:SuppliesSchema):
    logger.info(f"Datos: {jsonable_encoder(supplies)}, service: '/supplies', method: 'POST")
    db = Session()
    SuppliesService(db).create_supplies(supplies)
    return JSONResponse(content={"message":"supplies created", 'status_code': 200})

@supplies_router.put('/supplies{id}', tags=['supplies'])
def update_supplies(id: int, data: SuppliesSchema):
    logger.info(f"Datos: {jsonable_encoder(data)}, service: '/supplies', method: 'PUT")
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "supplies not found", "status_code": 400})
    SuppliesService(db).update_supplies(id,data)
    return JSONResponse(content={"message": "supplies updated successfully", "status_code": 200})

@supplies_router.delete('/supplies{id}', tags=['supplies'])
def delete_supplies(id:int):
    logger.info(f"ID: {id}, service: '/supplies', method: 'DELETE")
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"supplies don't found", "status_code": 404})
    SuppliesService(db).delete_supplies(id)
    return JSONResponse(content={"message":"supplies deleted succesfully","status_code": 200})