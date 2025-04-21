# FastAPI-Basic
This project demonstrates a simple **CRUD (Create, Read, Update, Delete)** REST API using **FastAPI** and **SQLAlchemy**.

## 🛠 Tech Stack

- **FastAPI** - Web framework for building APIs
- **SQLAlchemy** - ORM (Object Relational Mapper)
- **SQLite** - Lightweight database for development
- **Pydantic** - Data validation & settings management

## 🚀 Features

- Create new items (POST)
- Read all or specific items (GET)
- Update existing items (PUT)
- Delete items (DELETE)
- Auto-generated API Docs via Swagger (at `/docs`)
- SQLite database for quick setup

## 📂 Project Structure
![image](https://github.com/user-attachments/assets/75bc8deb-95ed-44b5-bfa8-a80ac7a7d7fd)


## ⚙️ Installation & Run
### 1. Clone the repo
git clone https://github.com/chavitdew/FastAPI-Basic.git<br>
cd FastAPI-Basic
### 2. Create virtual environment
python -m venv venv<br>
source venv/bin/activate   Windows: venv\Scripts\activate
### 3. Install dependencies
pip install -r requirements.txt
### 4. Run
fastapi dev main.py
