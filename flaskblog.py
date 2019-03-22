from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'Author':'Prudvi Bilakanti',
        'Content':'End to end machine learning flow',
        'Posted':'3/21/2019'
    },
{
        'Author':'Rudra Shrihaan',
        'Content':'End to end machine learning flow',
        'Posted':'3/22/2019'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)