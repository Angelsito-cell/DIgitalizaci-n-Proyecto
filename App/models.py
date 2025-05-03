from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    stock = Column(Integer, default=0)
    price = Column(Float)
    
    sales = relationship("SalesHistory", back_populates="product")

class SalesHistory(Base):
    __tablename__ = "sales_history"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    month = Column(Integer)
    sales = Column(Integer)
    
    product = relationship("Product", back_populates="sales")