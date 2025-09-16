from flask import Flask, render_template, request
from models import db, User

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Cricket"]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get("name")
    if not name:
        return render_template('error.html', message="Name missing.")
    sport = request.form.get("sport")
    if not sport:
        return render_template('error.html', message="Sport missing")
    if sport not in SPORTS:
        return render_template('error.html', message="Invalid sport selected.")

    # Save to database instead of dict
    new_user = User(name=name, sport=sport)
    db.session.add(new_user)
    db.session.commit()

    return render_template('success.html', name=name, sport=sport)

@app.route('/registrants')
def registrants():
    # fetch from database instead of dict
    all_users = User.query.all()
    return render_template('registrants.html', registrants=all_users)

if __name__ == '__main__':
    app.run(debug=True)
