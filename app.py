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
employee=False
user_view="customer-ID"
empVisible=""
custVisible="active"

@app.route('/', methods=['GET', 'POST'])
def index():
    if(session):
        if(session["loggedin"]):
            global employee
            employee=session['employee']
            if(employee):
                return  render_template('empHome.html')
            else:
                return render_template('custHome.html')
    
    return render_template('index.html',username=user_view, msg='',emp=empVisible,cust=custVisible)


@app.route('/login/<string:emp>', methods=['GET', 'POST'])
def logas(emp):
    if(emp=="employee"):
        global empVisible       
        global custVisible        
        global employee
        global user_view
        custVisible=""
        employee=True
        user_view="Employee-ID"
        empVisible="active"
        return render_template('index.html',username=user_view, msg='',emp=empVisible,cust=custVisible)
    else:
       
        empVisible=""
        custVisible="active"
        employee=False
        user_view="Customer-ID"
        return render_template('index.html',username=user_view, msg='',emp=empVisible,cust=custVisible)

@app.route('/home', methods=['GET', 'POST'])
def login():
    if(session):
        if(session["loggedin"]):
            global employee
            employee=session['employee']
            if(employee):
                return  render_template('empHome.html')
            else:
                return render_template('custHome.html')
  



    msg = ''

    print(request.form)

    if request.method == 'POST' and 'id' in request.form and 'password' in request.form:

        

        username = request.form['id']
        password = request.form['password']
      
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        if(employee):
            cursor.execute('SELECT * FROM empstore WHERE user_id = %s AND password = %s', (username, password))
        else:
            cursor.execute('SELECT * FROM userstore WHERE user_id = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists 
        if account:
            # Creating session data
            session['loggedin'] = True
            session['username'] = account['user_id']
            session['employee']= employee

            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print(timestamp)
            if(employee):
                cursor.execute('UPDATE empstore SET timestamp = %s WHERE  user_id = %s;',(timestamp,account['user_id']))
            else:
                cursor.execute('UPDATE userstore SET timestamp = %s WHERE  user_id = %s;',(timestamp,account['user_id']))

            
            mysql.connection.commit()
            # Redirecting to home page
            if(employee):
                return  render_template('empHome.html')
            else:
                return render_template('custHome.html')
        else:
            # Account doesnt exist 
            
            msg = 'Incorrect username/password!!!'
    # Show the login form with message (if any)
    
    return render_template('index.html',username=user_view, msg=msg,emp=empVisible,cust=custVisible)



if __name__ == '__main__':
    app.run(debug=True)