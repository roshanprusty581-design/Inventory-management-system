from models.stock import Stock
from models.purchase import Purchase
from models.sale import Sale

def purchase_stock(session, product_id, quantity):
    stock = session.get(Stock, product_id)

    if stock:
        stock.quantity += quantity
    else:
        stock = Stock(product_id=product_id, quantity=quantity)
        session.add(stock)

    session.add(Purchase(product_id=product_id, quantity=quantity))
    session.commit()


def sell_stock(session, product_id, quantity):
    stock = session.get(Stock, product_id)

    if not stock or stock.quantity < quantity:
        print("❌ Not enough stock")
        return

    stock.quantity -= quantity
    session.add(Sale(product_id=product_id, quantity=quantity))
    session.commit()
