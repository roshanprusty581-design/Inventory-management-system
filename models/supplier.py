from sqlalchemy import Column, Integer, String
from models.base import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact = Column(String(50))
    email = Column(String(100))
