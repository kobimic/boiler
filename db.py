from config import configuration
from logger import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    configuration.sql_url, connect_args={"check_same_thread": False}
)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
logger.info("DB init done")
