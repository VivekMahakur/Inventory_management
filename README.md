
# 📦 Inventory Management System

A simple, efficient, and **responsive web-based inventory manager** built with **Django** and **Bootstrap**, perfect for small businesses, shops, or warehouse operations.

## 🚀 Features

  * **🔐 Authentication:** Role-based login system separating **Admin** and standard **User** access.
  * **📊 Inventory Management (CRUD):** Complete **C**reate, **R**ead, **U**pdate, and **D**elete operations for managing product details and viewing the product list.
  * **🗄️ Database:** Clean and optimized SQL-backed storage for all inventory data.
  * **💻 Responsive UI:** Seamless user experience across **desktop** and **mobile** devices thanks to **Bootstrap**.

-----

## 🛠️ Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, Bootstrap |
| **Backend** | **Django** (Python) |
| **Database** | SQL (SQLite / PostgreSQL) |
| **Tools** | Git |

-----

## ⚙️ Installation & Setup

Follow these steps to get the project up and running locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/VivekMahakur/Inventory-Management-System.git
cd Inventory-Management-System
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For Linux/Mac
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the server

```bash
python manage.py runserver
```

### 6️⃣ Access in browser

Open your web browser and navigate to:
👉 **`http://127.0.0.1:8000/`**
