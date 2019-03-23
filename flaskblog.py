from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ea3b631e1d2ad4ea9ad1c900c4daeea8'

posts = [
    {
        'Author': 'Prudvi Bilakanti',
        'Content': 'End to end machine learning flow',
        'Posted': '3/21/2019'
    },
{
        'Author': 'Rudra Shrihaan',
        'Content': 'End to end machine learning flow',
        'Posted': '3/22/2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account has been successfully create for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__  ==  '__main__':
    app.run(debug=True)