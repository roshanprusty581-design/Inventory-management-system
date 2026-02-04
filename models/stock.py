from sqlalchemy import Column, Integer, ForeignKey
from models.base import Base

class Stock(Base):
    __tablename__ = "stock"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    quantity = Column(Integer, nullable=False)
