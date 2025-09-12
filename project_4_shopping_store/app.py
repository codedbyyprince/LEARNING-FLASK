# app.py
from flask import Flask, render_template, request, redirect
from models import db, Book

app = Flask(__name__)

# Config (change for PostgreSQL accordingly)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prince_user:password@localhost/store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    books = Book.query.all()  # READ
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    new_book = Book(title=title)
    db.session.add(new_book)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
