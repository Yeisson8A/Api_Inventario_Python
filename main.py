from fastapi import FastAPI
import uvicorn
from routes.routes_supplier import supplier_router
from routes.routes_supplies import supplies_router
from routes.routes_product import product_router
from middlewares.error_handler import Errorhandler
from db.config import engine,Base

app = FastAPI()
app.title = "Sistema de Inventarios"
app.description="Operaciones CRUD usando una API"
app.version = "1.0.0"

# Agregar rutas y middleware
app.add_middleware(Errorhandler)
app.include_router(supplier_router)
app.include_router(supplies_router)
app.include_router(product_router)  

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)