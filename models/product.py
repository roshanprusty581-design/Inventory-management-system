from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from models.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    low_stock_threshold = Column(Integer, default=5)
