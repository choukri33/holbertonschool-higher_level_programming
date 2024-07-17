from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    source = request.args.get('source')
    item_id = request.args.get('id')

    if source == 'json':
        items = get_items_from_json(item_id)
    elif source == 'csv':
        items = get_items_from_csv(item_id)
    elif source == 'sql':
        items = get_items_from_sql(item_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    return render_template('product_display.html', items=items)

def get_items_from_json(item_id=None):
    with open('items.json', 'r') as file:
        data = json.load(file)
    items = data['items']
    if item_id:
        items = [item for item in items if item['id'] == int(item_id)]
    return items if items else ["Product not found"]

def get_items_from_csv(item_id=None):
    items = []
    with open('items.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = {"id": int(row['id']), "name": row['name'], "category": row['category'], "price": float(row['price'])}
            items.append(item)
    if item_id:
        items = [item for item in items if item['id'] == int(item_id)]
    return items if items else ["Product not found"]

def get_items_from_sql(item_id=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    if item_id:
        cursor.execute("SELECT * FROM Products WHERE id=?", (item_id,))
    else:
        cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    items = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    return items if items else ["Product not found"]

if __name__ == '__main__':
    app.run(debug=True, port=5000)
