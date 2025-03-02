from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Dili Dili',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 25 2025'
    },
    {
        'author': 'Abhi Abhi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 26 2025'
    },
    {
        'author': 'Dini Dini',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'February 27 2025'
    },
    {
        'author': 'Danu Danu',
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'date_posted': 'February 28 2025'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
    