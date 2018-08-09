from flask import Flask, session, flash, redirect, render_template, request
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = '1n1@@4dscn%@T721fb@%Dewdsc2323?'



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    present = datetime.now()
    # place all inputs from registration form into a session variable
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    session['birth_date'] = request.form['birth_date']

    # Clean up code by placing all session variables into a clear show variable
    email = session['email']
    first = session['first_name']
    last = session['last_name']
    password = session['password']
    confirm = session['confirm_password']
    birth = session['birth_date']
    
    #Confirm all variables are working
    print email, first, last, password, confirm
    
    #Validation
    #For email
    if not EMAIL_REGEX.match(email):
        flash('Email field is not valid', 'error')
        return redirect('/')
    #For First Name
    if first == '':
        flash('Name field can not be blank', 'error')
    elif not first.isalpha():
        flash('First Name field can not contain number values', 'error')
        return redirect('/')
    #For Last Name
    if last == '':
        flash('Last Name field can not be blank', 'error')
    elif not last.isalpha():
        flash('Last Name field can not contain number values', 'error')
        return redirect('/')
    #For Password
    if len(password) <= 8:
        flash('Password must contain more than 8 characters', 'error')
        return redirect('/')
    #For Confirm Password
    if confirm != password:
        flash('Password and Confirm Password do not match', 'error')
    elif not re.search('[0-9]', password):
        flash('Password must contain atleast one number value', 'error')
    elif not re.search('[A-Z]', password):
        flash('Password must contain atleast one capital letter', 'error')
        return redirect('/')
    #For Birth Date
    if  datetime.strptime(birth, '%Y-%m-%d') > present:
        flash('Birth Date is not valid')
        return redirect('/')
    flash('Thanks for submitting your information')
    
    return redirect('/')
app.run(debug=True)