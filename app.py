from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hotspots.json')
def hotspots():
    return send_from_directory(directory='static', path='hotspots.json')

if __name__ == '__main__':
    app.run(debug=True)

