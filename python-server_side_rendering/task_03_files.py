from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source')

    products = data if isinstance(data, list) else data['items']

    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
