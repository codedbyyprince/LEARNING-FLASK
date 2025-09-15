from flask import Flask, render_template, request, redirect, session
from models import db, Show
from flask_session import Session

app = Flask(__name__)

# Config (change for PostgreSQL accordingly)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prince_user:password@localhost/shows'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# create tables
with app.app_context():
    db.create_all()

app.config["SESSION_PERMANENT"] = False  # or True, depending on your needs
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


app.route('/')
def index():
    shows = Show.query.all()  # READ
    return render_template('index.html', shows=shows)

@app.route("/favorites" , methods=["GET", "POST"])
