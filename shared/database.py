from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATA_BASE_URL = "postgresql://postgres:senha123@localhost/supermercado_filip_db"
engine = create_engine(SQLALCHEMY_DATA_BASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()