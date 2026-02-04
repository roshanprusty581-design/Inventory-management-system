from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from models.base import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    sale_date = Column(DateTime, server_default=func.now())
