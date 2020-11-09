from flask import Flask, render_template, request, redirect, session, url_for, g
import model

app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key = 'dontstare'


username = ''
users = model.get_all_users()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'username' in session:
            g.user = session['username']
            return redirect('dashboard')
        return render_template('index.html')
    
    return render_template('index.html')


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        session.pop('username', None)
        user, password = request.form['username'], request.form['password']
        if model.auth_user(user, password):
            session['username'] = user
            return redirect('/dashboard')

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


@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('temp.html')


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
