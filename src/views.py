from flask import Blueprint, request
from pydantic import BaseModel, Field
from models import Book
from database import db


class BookSchema(BaseModel):
    name: str = Field(..., max_length=255)
    author: str = Field(..., max_length=255)
    description: str = Field(...)
    book_count: int = Field(...)


book_blueprint = Blueprint('books', __name__)


@book_blueprint.route('/book', methods=['POST'])
def add_book():
    book_schema = BookSchema(**request.json)
    new_book = Book(name=book_schema.name, author=book_schema.author, description=book_schema.description,
                    book_count=book_schema.book_count)

    db.session.add(new_book)
    db.session.commit()

    return {'status': "Book added to inventory successfully"}


@book_blueprint.route('/book/search/<name>', methods=['GET'])
def search_book(name):
    book = Book.query.filter_by(name=name).first()
    if book is None:
        return {"error": "Book not found"}, 404

    return {
        'name': book.name,
        'author': book.author,
        'description': book.description,
        'book_count': book.book_count
    }


@book_blueprint.route('/book/availability/<id>', methods=['GET'])
def check_availability(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book not found"}, 404

    return {
        'name': book.name,
        'author': book.author,
        'description': book.description,
        'book_count': book.book_count,
        'is_available': book.book_count > 0
    }


@book_blueprint.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return {'books': [
        {'name': book.name, 'author': book.author, 'description': book.description, 'book_count': book.book_count}
        for book in books]}


@book_blueprint.route('/book/increase/<int:book_id>', methods=['PUT'])
def increase_book_count(book_id):
    quantity = request.json.get('quantity', 1)
    book = Book.query.get(book_id)
    if book is None:
        return {"error": "Book not found"}, 404

    book.book_count += quantity
    db.session.commit()

    return {'book_count': book.book_count}


@book_blueprint.route('/book/decrease/<int:book_id>', methods=['PUT'])
def decrease_book_count(book_id):
    quantity = request.json.get('quantity', 1)
    book = Book.query.get(book_id)
    if book is None:
        return {"error": "Book not found"}, 404

    if book.book_count < quantity:
        return {"error": "Not enough books in stock"}, 400

    book.book_count -= quantity
    db.session.commit()

    return {'book_count': book.book_count}
