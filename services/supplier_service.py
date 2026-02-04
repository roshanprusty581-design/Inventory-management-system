from models.supplier import Supplier

def add_supplier(session, name, contact, email):
    supplier = Supplier(name=name, contact=contact, email=email)
    session.add(supplier)
    session.commit()
