from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Product

router = APIRouter(prefix="/inventory", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@router.post("/")
def add_product(name: str, stock: int, price: float, db: Session = Depends(get_db)):
    product = Product(name=name, stock=stock, price=price)
    db.add(product)
    db.commit()
    return {"message": "Producto agregado"}
