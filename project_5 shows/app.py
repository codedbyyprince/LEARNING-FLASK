from flask import Flask, render_template, request
from flask_session import Session
from models import db, Show
import csv

app = Flask(__name__)

# Config (PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prince_user:password@localhost/shows'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Initialize db with app
db.init_app(app)

with app.app_context():
    # Create tables
    db.create_all()

    # Load CSV only if table is empty (prevents duplicates)
    if Show.query.count() == 0:
        with open('/media/prince/5A4E832F4E83034D/Flask learning/project_5 shows/imdb_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            shows = [Show(title=row['title'], rating=float(row['rating'])) for row in reader]

        db.session.bulk_save_objects(shows)
        db.session.commit()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')  # get ?q= from URL
    if query:
        # case-insensitive partial match
        shows = Show.query.filter(Show.title.ilike(f'%{query}%')).all()
    else:
        shows = []
    return render_template('search.html', shows=shows, query=query)


if __name__ == '__main__':
    app.run(debug=True)
