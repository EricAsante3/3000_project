from flask import Flask, request, jsonify
from script import test
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# backend of site
@app.route('/')
def home(): 
    return "3000_project"


# front end flask
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # or request.form for form data
    text = data.get('text')
    return jsonify(test(text))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5123)
