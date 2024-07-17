from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page template
    return render_template('index.html')

@app.route('/about')
def about():
    # Render the about page template
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Render the contact page template
    return render_template('contact.html')

# Route to display the items
@app.route('/items')
def items():
    # Read data from the JSON file
    with open('items.json', 'r') as file:
        data = json.load(file)
    
    # Pass the data to the template
    return render_template('items.html', items=data['items'])

if __name__ == '__main__':
    # Run the Flask application in debug mode on port 5000
    app.run(debug=True, port=5000)
