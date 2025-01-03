from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mssql+pyodbc://LAPTOP-19URHKFN\\SQLEXPRESS/DBInventario?driver=SQL+Server+Native+Client+11.0"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 