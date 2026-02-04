from sqlalchemy import select
from models.stock import Stock
from models.product import Product

def check_low_stock(session):
    stmt = (
        select(Product.name, Stock.quantity, Product.low_stock_threshold)
        .join(Stock, Product.id == Stock.product_id)
        .where(Stock.quantity <= Product.low_stock_threshold)
    )

    result = session.execute(stmt).all()

    if result:
        print("\n⚠️ LOW STOCK ALERT ⚠️")
        for row in result:
            print(f"{row.name} → {row.quantity}")
    else:
        print("✅ Stock levels are OK")
