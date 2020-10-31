from flask import Flask, render_template

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

app.run(debug=True)