from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Product catalog with images
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 70000,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
    },
    {
        "id": 2,
        "name": "Mobile Phone",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 4000,
        "image": "https://images.unsplash.com/photo-1518441902117-f9b88d5b7d8a"
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 12000,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    }
]

cart = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Shop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #141e30, #243b55);
            margin: 0;
            padding: 0;
            color: #333;
        }
        .navbar {
            background: #111;
            padding: 15px;
            color: white;
            text-align: center;
            font-size: 22px;
            letter-spacing: 1px;
        }
        .container {
            width: 90%;
            margin: 30px auto;
        }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .product {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }
        .product:hover {
            transform: scale(1.03);
        }
        .product img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }
        .product-details {
            padding: 15px;
        }
        .price {
            color: #28a745;
            font-weight: bold;
            margin: 8px 0;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #28a745;
            border: none;
            color: white;
            font-size: 15px;
            cursor: pointer;
            border-radius: 4px;
        }
        button:hover {
            background: #218838;
        }
        .cart {
            background: white;
            padding: 20px;
            margin-top: 40px;
            border-radius: 8px;
        }
        .cart h2 {
            margin-top: 0;
        }
        .cart-item {
            border-bottom: 1px solid #ddd;
            padding: 8px 0;
        }
        .total {
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="navbar">
    🛒 DevOps Online Shopping Platform
</div>

<div class="container">

    <div class="products">
        {% for p in products %}
        <div class="product">
            <img src="{{ p.image }}" alt="{{ p.name }}">
            <div class="product-details">
                <h3>{{ p.name }}</h3>
                <div class="price">₹{{ p.price }}</div>
                <form method="post" action="/add/{{ p.id }}">
                    <button>Add to Cart</button>
                </form>
            </div>
        </div>
        {% endfor %}
    </div>

    <div class="cart">
        <h2>🧾 Cart Summary</h2>
        {% if cart %}
            {% for c in cart %}
            <div class="cart-item">
                {{ c.name }} - ₹{{ c.price }}
            </div>
            {% endfor %}
            <div class="total">Total: ₹{{ total }}</div>
        {% else %}
            <p>Your cart is empty</p>
        {% endif %}
    </div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    total = sum(item["price"] for item in cart)
    return render_template_string(HTML, products=products, cart=cart, total=total)

@app.route("/add/<int:pid>", methods=["POST"])
def add_to_cart(pid):
    for p in products:
        if p["id"] == pid:
            cart.append(p)
            break
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
