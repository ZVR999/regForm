from flask import Flask, session, flash, redirect, render_template, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = '1n1@@4dscn%@T721fb@%Dewdsc2323?'



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    
    # place all inputs from registration form into a session variable
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']

    # Clean up code by placing all session variables into a clear show variable
    email = session['email']
    first = session['first_name']
    last = session['last_name']
    password = session['password']
    confirm = session['confirm_password']
    
    #Confirm all variables are working
    print type(email), first, last, password, confirm
    
    #Validation
    #For email
    if not EMAIL_REGEX.match(email):
        flash('Email field is not valid')
        return redirect('/')
    #For First Name
    if first == '':
        flash('Name field can not be blank')
    elif not first.isalpha():
        flash('First Name field can not contain number values')
        return redirect('/')
    #For Last Name
    if last == '':
        flash('Last Name field can not be blank')
    elif not last.isalpha():
        flash('Last Name field can not contain number values')
        return redirect('/')
    #For Password
    return redirect('/')
app.run(debug=True)