from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message='welcome')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if model.auth_user(username, password):
            return redirect('/dashboard')
        else:
            return render_template('login.html', message='login failed')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        if password1 != password2:
            return render_template('signup.html', message='passwords dont match')
        if model.user_exists(username):
            return render_template('signup.html', message='user already exists')

        model.create_user(username, password1)
        return redirect('/login')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')


@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


app.run(debug=True)
