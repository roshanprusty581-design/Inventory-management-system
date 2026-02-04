from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from models.base import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    purchase_date = Column(DateTime, server_default=func.now())
