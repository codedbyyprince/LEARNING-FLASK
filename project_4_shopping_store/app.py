# app.py
from flask import Flask, render_template, request, redirect, session
from models import db, Book
from flask_session import Session

app = Flask(__name__)

# Config (change for PostgreSQL accordingly)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prince_user:password@localhost/store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# create tables
with app.app_context():
    db.create_all()

app.config["SESSION_PERMANENT"] = False  # or True, depending on your needs
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/')
def index():
    books = Book.query.all()  # READ
    return render_template('index.html', books=books)

@app.route("/cart" , methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect('/cart')
    books = Book.query.filter(Book.id.in_(session["cart"])).all()
    return render_template( 'cart.html' , books=books)



# @app.route('/add', methods=['POST'])
# def add():
#     title = request.form['title']
#     new_book = Book(title=title)
#     db.session.add(new_book)
#     db.session.commit()
#     return redirect('/')

# @app.route('/delete/<int:id>')
# def delete(id):
#     book = Book.query.get(id)
#     db.session.delete(book)
#     db.session.commit()
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
