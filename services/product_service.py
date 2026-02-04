from models.product import Product

def add_product(session, name, price, supplier_id, threshold):
    product = Product(
        name=name,
        price=price,
        supplier_id=supplier_id,
        low_stock_threshold=threshold
    )
    session.add(product)
    session.commit()
