from flask import Flask, render_template , request, redirect, url_for, session
from flask_fontawesome import FontAwesome

from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime 
import time




app = Flask(__name__)
fa = FontAwesome(app)
app.secret_key = 'secret_key_007'

# database connection details 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'manager'
app.config['MYSQL_PASSWORD'] = 'manager'
app.config['MYSQL_DB'] = 'bms'


mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if(session):
        if(session["loggedin"]):
            return "hello"
    return render_template('index.html', msg='')


@app.route('/login/', methods=['GET', 'POST'])
def login():

    if(session):
        if(session["loggedin"]):
            return "hello"
  
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
      
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userstore WHERE user_id = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists 
        if account:
            # Creating session data
            session['loggedin'] = True
            session['username'] = account['user_id']

            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print(timestamp)
            cursor.execute('UPDATE userstore SET timestamp = %s WHERE  user_id = %s;',(timestamp,account['user_id']))
            mysql.connection.commit()
            # Redirecting to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist 
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)