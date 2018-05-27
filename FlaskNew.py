from flask import Flask, render_template, flash, redirect, request, url_for, session, make_response
from wtforms import Form, StringField, TextAreaField, validators, PasswordField, DecimalField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from passlib.hash import sha256_crypt
from pymysql import escape_string as thwart
import pymysql

import gc
from dbconnect import connection

import pushdata, statistics


app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'DontTellAnyone'


@app.route('/')
def home():
    return render_template('home.html')

class QueryForm(FlaskForm):
    # inputquery = TextAreaField(u'Input Query', validators=[validators.input_required()])
    text = TextAreaField('Enter the Search Query here', validators=[validators.input_required()])

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.input_required(), validators.EqualTo('confirm', message="Passwords need to match")])
    confirm = PasswordField('Confirm Password')

class TestForm(Form):
    raspi_ip= StringField('Raspberry Pi IP', [validators.IPAddress(ipv4=True)])


@app.route('/dct', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        return 'Query Submitted Successfully'
    # return redirect(url_for('dct_results'))
    return render_template('dct.html', form=form)

@app.route('/dct_results', methods=['GET', 'POST'])
def dct_results():
    submit_text = request.form['text']
    print(submit_text)
    # with open("temp.txt", "w") as fo:
    #     fo.write(submit_text)
    #     fo.flush()
    return render_template('dct_results.html', text=submit_text)

@app.route('/login', methods=['GET','POST'])
def login_page():
    error=''
    try:
        c, conn = connection()
        if request.method == "POST":
            data = c.execute("SELECT * FROM users WHERE username = %s",
                             [thwart(request.form['username'])])
            print (data)

            data = c.fetchone()[2]

            if data and sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']


                return redirect(url_for("dashboard"))
            else:
                flash("Invalid credentials, try again.")

        gc.collect()
        return render_template("login.html", error=error)

    except Exception as e:
        flash("Invalid credentials, try again.")    
        return render_template("login.html", error=error)


@app.route('/register', methods=["GET", "POST"])
def register_page():
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username =(%s)",
                          (thwart(username)))

            if x:
                flash("Username already taken. Please choose another")
                return render_template('register.html', form=form)
            else:
                c.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                          (thwart(username), thwart(password), thwart(email)))
                conn.commit()
                flash("Thanks for registering")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('home'))

        return render_template("register.html", form=form)

@app.route('/dashboard',  methods=["GET", "POST"])
def dashboard():
    error=''
    if session.get('logged_in') == False:
        error = "Please login first to access the dashboard"
        # print(session.get('logged_in'))
        render_template("home.html")
    elif session.get('logged_in') == True:
        # print(session.get('logged_in'))
        remoteuserip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        print("Remote user " + remoteuserip + " has connected")
    controller = request.form.get('controller')
    target = request.form.get('target')
    testtype = request.form.get('testtype')
    # print(str(controller))
    # print(str(target))
    # print(str(testtype))

    if request.method == 'POST':
        pushdata.pushfiles(target)
        flash ('Test Complete')

    (testnumsd,testnumpd,testnumtotal) = statistics.numoftests()
    (avgrdspd1, avgwrspd1, avgrdspd2, avgwrspd2) = statistics.avgspeed()



    return render_template("dashboard.html", error=error, testnumsd=testnumsd, testnumpd=testnumpd, testnumtotal=testnumtotal, avgrdspd1=avgrdspd1, avgwrspd1=avgwrspd1, avgrdspd2=avgrdspd2, avgwrspd2=avgwrspd2)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    # print(session.get('logged_in'))
    flash("You have logged out.")
    return redirect(url_for('home'))



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)