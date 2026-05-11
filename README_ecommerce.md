# 🛒 NEXUS Store — E-Commerce Application

**BLM3522 Cloud Computing Course | Project 4**  
**Şeyma Kula**

---

## 📌 About the Project

NEXUS Store is a full-stack e-commerce web application built with Flask and deployed on AWS EC2. It features product listing, search, category filtering, cart management, and order placement.

**Architecture:**
```
Browser (index.html)
        ↓ HTTP
Flask Backend (AWS EC2)
        ↓
SQLite Database
```

---

## 🏗️ System Architecture

| Component | Technology | Description |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | Dark theme, responsive UI |
| Backend | Python Flask | RESTful API |
| Database | SQLite | Product and order storage |
| Cloud | AWS EC2 (t3.micro) | Ubuntu 24.04 LTS |
| Process Manager | systemd | Auto-restart on reboot |

---

## 📁 File Structure

```
nexus-store/
│
├── app.py          # Flask backend + REST API
├── index.html      # Frontend (dark theme e-commerce UI)
├── README.md
└── .gitignore
```

---

## 🛍️ Features

| Feature | Description |
|---|---|
| Product Listing | Display all products with emoji icons |
| Search | Real-time search by name, description, category |
| Category Filter | Filter by Computer, Phone, Accessory |
| Add to Cart | Add products with animated feedback |
| Cart Modal | View cart items and total price |
| Order Placement | Complete order with name and email |
| Order Confirmation | Success message after order |

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/products | List all products |
| GET | /api/products/\<id\> | Get single product |
| POST | /api/orders | Create new order |
| GET | /api/orders | List all orders |
| POST | /api/seed | Seed sample products |

---

## ⚙️ Setup and Usage

### 1. Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy flask-cors python-dotenv
python3 app.py
```

Open: `http://localhost:80`

### 2. AWS EC2 deployment

```bash
git clone https://github.com/seymakula/nexus-store.git
cd nexus-store
python3 -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy flask-cors gunicorn python-dotenv psycopg2-binary
sudo venv/bin/python3 app.py
```

---

## ☁️ AWS Configuration

| Setting | Value |
|---|---|
| Instance Name | nexus-store-server |
| AMI | Ubuntu Server 24.04 LTS |
| Instance Type | t3.micro (Free Tier) |
| Region | eu-central-1 (Frankfurt) |
| Open Ports | 22 (SSH), 80 (HTTP) |
| Public IP | 3.79.231.248 |
| Live URL | http://3.79.231.248 |

---

## 🔒 Security Note

Database files and virtual environment are excluded from git via `.gitignore`.

---

## 📚 References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [systemd Service](https://www.freedesktop.org/wiki/Software/systemd/)
