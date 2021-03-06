from flask import Blueprint, render_template, request, redirect, url_for, flash
from journal_refuge.forms import UserLoginForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])

def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            # TODO: add user to database

            flash(f'You have successfully created a user account for {email}.', "user-created")

            return redirect(url_for('site.home'))
        
    except:
        raise Exception('Invalid Form Data: Please check your form...')

    return render_template('signup.html', form = form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('signin.html')
