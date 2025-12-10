from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
items = [
    {"id": 1, "name": "Apple", "price": 10},
    {"id": 2, "name": "Banana", "price": 5},
]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "name and price are required"}), 400

    new_id = max([item["id"] for item in items] or [0]) + 1
    new_item = {"id": new_id, "name": data["name"], "price": data["price"]}
    items.append(new_item)
    return jsonify(new_item), 201


if __name__ == "__main__":
    # For local development only
    app.run(host="0.0.0.0", port=5000, debug=True)
