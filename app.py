from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(200))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)
    total_price = db.Column(db.Float)
    status = db.Column(db.String(20), default='pending')

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id, 'name': p.name, 'description': p.description,
        'price': p.price, 'stock': p.stock, 'image_url': p.image_url
    } for p in products])

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    p = Product.query.get_or_404(id)
    return jsonify({'id': p.id, 'name': p.name, 'description': p.description,
        'price': p.price, 'stock': p.stock, 'image_url': p.image_url})

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    product = Product.query.get_or_404(data['product_id'])
    order = Order(
        customer_name=data['customer_name'],
        customer_email=data['customer_email'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        total_price=product.price * data['quantity']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Sipariş alındı!', 'order_id': order.id}), 201

@app.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'id': o.id, 'customer_name': o.customer_name,
        'customer_email': o.customer_email, 'quantity': o.quantity,
        'total_price': o.total_price, 'status': o.status
    } for o in orders])

@app.route('/api/seed', methods=['POST'])
def seed():
    products = [
        Product(name='Laptop', description='15.6 inch Full HD laptop, 16GB RAM, 512GB SSD', price=12999.99, stock=10, image_url='https://via.placeholder.com/300x200?text=Laptop'),
        Product(name='Telefon', description='6.5 inch AMOLED ekran, 128GB depolama', price=7499.99, stock=25, image_url='https://via.placeholder.com/300x200?text=Telefon'),
        Product(name='Kulaklık', description='Kablosuz, gürültü önleyici, 30 saat pil', price=1299.99, stock=50, image_url='https://via.placeholder.com/300x200?text=Kulaklik'),
        Product(name='Tablet', description='10.1 inch, 64GB, WiFi + 4G', price=4999.99, stock=15, image_url='https://via.placeholder.com/300x200?text=Tablet'),
        Product(name='Akıllı Saat', description='GPS, kalp atışı ölçer, su geçirmez', price=2499.99, stock=30, image_url='https://via.placeholder.com/300x200?text=Saat'),
    ]
    for p in products:
        db.session.add(p)
    db.session.commit()
    return jsonify({'message': 'Ürünler eklendi!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5002)
