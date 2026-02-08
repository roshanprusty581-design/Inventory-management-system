
# 📦 Inventory Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red.svg)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> A modular and scalable **Inventory Management System** built using **Python + SQLAlchemy**, designed to manage products, suppliers, stock, purchases, and sales efficiently.

---

## ✨ Overview

This project is a **backend-focused inventory management system** following clean architecture principles.  
It separates **configuration**, **database models**, and **business logic (services)** to keep the codebase maintainable, extensible, and production-ready.

The system supports:
- Product management
- Supplier management
- Stock tracking
- Sales & purchase handling
- Low-stock alert logic

---

## 🧠 Key Features

✅ Product CRUD operations  
✅ Supplier management  
✅ Stock quantity tracking  
✅ Sales & purchase records  
✅ Low-stock alert service  
✅ SQLite database integration  
✅ SQLAlchemy ORM  
✅ Clean service-based architecture  

---

## 🏗️ Project Architecture

The project follows a **layered architecture**:

```bash
Inventory-management-system/
│
├── config/
│   └── database.py        # Database engine & session setup
│
├── models/
│   ├── base.py            # Base declarative model
│   ├── product.py         # Product table
│   ├── supplier.py        # Supplier table
│   ├── stock.py           # Stock table
│   ├── purchase.py        # Purchase records
│   └── sale.py            # Sale records
│
├── services/
│   ├── product_service.py # Product business logic
│   ├── supplier_service.py# Supplier business logic
│   ├── stock_service.py   # Stock management logic
│   └── alert_service.py   # Low stock alerts
│
├── main.py                # Application entry point
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
````

---

## 🛠️ Tech Stack

| Technology     | Usage                      |
| -------------- | -------------------------- |
| **Python**     | Core programming language  |
| **SQLAlchemy** | ORM & database interaction |
| **SQLite**     | Lightweight database       |
| **VS Code**    | Development environment    |

---

## ⚙️ Database Configuration

Database is configured using **SQLAlchemy**:

```python
DATABASE_URL = "sqlite:///inventory.db"
```

* Automatically creates `inventory.db`
* SQL queries can be logged using `echo=True`
* Session handled via `sessionmaker`

---

## 🚀 Getting Started

Follow these steps to run the project locally.

###  Prerequisites

* Python 3.8+
* pip installed

---

###  Installation

 Clone the repository

```bash
git clone https://github.com/roshanprusty581-design/Inventory-management-system.git
cd Inventory-management-system
```

 Install dependencies

```bash
pip install -r requirements.txt
```

 Run the application

```bash
python main.py
```

---

## 🧪 Example Use Cases

* Add new products and suppliers
* Increase stock via purchases
* Reduce stock via sales
* Check available stock for a product
* Trigger alerts when stock is low

This system can be easily extended to:

* REST APIs (Flask / FastAPI)
* Authentication
* Reports & analytics
* Frontend integration

---

## 🔮 Future Enhancements

🚀 Planned improvements:

* REST API with FastAPI
* JWT Authentication
* Role-based access
* Web dashboard
* Docker support
* PostgreSQL / MySQL support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch

```bash
git checkout -b feature/your-feature
```

3. Commit changes

```bash
git commit -m "Add your feature"
```

4. Push & create a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it.

---

## 👨‍💻 Author

**Roshan Prusty**
🔗 GitHub: [roshanprusty581-design](https://github.com/roshanprusty581-design)

---

⭐ If you like this project, **give it a star** — it really helps!

```
```

