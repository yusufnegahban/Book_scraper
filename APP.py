from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:10011001@localhost:5432/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(100))
    price = db.Column(db.String(20))
    availability = db.Column(db.String(100))
    isbn = db.Column(db.String(50))
    publish_date = db.Column(db.DateTime)

# Web page: main page with pagination and search
@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", "")

    query = Book.query
    if search:
        query = query.filter(or_(
            Book.title.ilike(f"%{search}%"),
            Book.author.ilike(f"%{search}%")
        ))

    books_paginated = query.order_by(Book.id).paginate(page=page, per_page=10)
    return render_template("index.html", books=books_paginated, search=search)

# Web page: book detail page
@app.route("/book/<int:book_id>")
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book_detail.html", book=book)

# REST API: get list of books (JSON)
@app.route("/api/books")
def api_books():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", "")

    query = Book.query
    if search:
        query = query.filter(or_(
            Book.title.ilike(f"%{search}%"),
            Book.author.ilike(f"%{search}%")
        ))

    books_paginated = query.order_by(Book.id).paginate(page=page, per_page=10)
    books = [{
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "price": b.price,
        "availability": b.availability,
        "isbn": b.isbn,
        "publish_date": b.publish_date.isoformat() if b.publish_date else None
    } for b in books_paginated.items]

    return jsonify({
        "page": page,
        "total_pages": books_paginated.pages,
        "total_books": books_paginated.total,
        "books": books
    })

# REST API: get details of one book (JSON)
@app.route("/api/book/<int:book_id>")
def api_book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "price": book.price,
        "availability": book.availability,
        "isbn": book.isbn,
        "publish_date": book.publish_date.isoformat() if book.publish_date else None
    })

if __name__ == "__main__":
    app.run(debug=True)
