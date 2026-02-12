from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# Unique Experience Catalog
experiences = [
    {
        "id": 1,
        "name": "Zero Gravity Experience",
        "price": 150000,
        "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa"
    },
    {
        "id": 2,
        "name": "Volcano Edge Camping",
        "price": 95000,
        "image": "https://images.unsplash.com/photo-1501785888041-af3ef285b470"
    },
    {
        "id": 3,
        "name": "AI Dream Simulation",
        "price": 50000,
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
    },
    {
        "id": 4,
        "name": "Underwater Meditation",
        "price": 80000,
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    }
]

cart = []

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>CosmicX - Beyond Reality</title>
<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

.navbar {
    padding: 20px;
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    background: rgba(0,0,0,0.6);
    letter-spacing: 2px;
}

.container {
    width: 90%;
    margin: 40px auto;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
}

.card {
    background: rgba(255,255,255,0.08);
    border-radius: 12px;
    overflow: hidden;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
}

.card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.details {
    padding: 20px;
}

.price {
    color: #00ffcc;
    font-weight: bold;
    margin: 10px 0;
}

button {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 6px;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    cursor: pointer;
    font-weight: bold;
}

button:hover {
    opacity: 0.85;
}

.cart {
    margin-top: 50px;
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 12px;
}

.total {
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
    color: #00ffcc;
}
</style>
</head>
<body>

<div class="navbar">
🌌 CosmicX – Book Beyond Reality
</div>

<div class="container">

<div class="cards">
{% for e in experiences %}
<div class="card">
    <img src="{{ e.image }}">
    <div class="details">
        <h3>{{ e.name }}</h3>
        <div class="price">₹{{ e.price }}</div>
        <form method="post" action="/add/{{ e.id }}">
            <button>Reserve Experience</button>
        </form>
    </div>
</div>
{% endfor %}
</div>

<div class="cart">
<h2>🚀 Your Bookings</h2>
{% if cart %}
    {% for c in cart %}
        <div>{{ c.name }} - ₹{{ c.price }}</div>
    {% endfor %}
    <div class="total">Total: ₹{{ total }}</div>
{% else %}
    <p>No experiences selected yet.</p>
{% endif %}
</div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    total = sum(item["price"] for item in cart)
    return render_template_string(HTML, experiences=experiences, cart=cart, total=total)

@app.route("/add/<int:eid>", methods=["POST"])
def add_to_cart(eid):
    for e in experiences:
        if e["id"] == eid:
            cart.append(e)
            break
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
