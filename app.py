from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'boooks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    author = db.Column(db.String(255))
    description = db.Column(db.Text)
    book_count = db.Column(db.Integer)

    def json(self):
        return {'id': self.id, 'name': self.name, 'author': self.author, 'description': self.description,
                'book_count': self.book_count}


with app.app_context():
    db.create_all()


# Test api
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'hey there! This is test api for product service! :)'}), 200)


# Create a Book
@app.route('/book', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_book = Book(name=data['name'], author=data['author'], description=data['description'],
                        book_count=data['book_count'])
        db.session.add(new_book)
        db.session.commit()
        return make_response(jsonify({'message': 'Book successfully created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while adding book.'}), 500)


# Search for Book
@app.route('/book/search/<name>', methods=['GET'])
def search_book(name):
    try:
        book = Book.query.filter_by(name=name).first()
        return make_response(
            jsonify({'message': 'Book Data fetched successfully', 'Book': {'name': book.name,
                                                                           'author': book.author,
                                                                           'description': book.description,
                                                                           'book_count': book.book_count}}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while fetching Book Data.'}), 500)


# Get book availability
@app.route('/book/availability/<id>', methods=['GET'])
def check_availability(id):
    try:
        book = Book.query.get(id)
        if book is None:
            return {"error": "Book not found"}, 404
        else:
            return make_response(jsonify({'message': 'Book data found!', 'Book': {'name': book.name,
                                                                                  'author': book.author,
                                                                                  'description': book.description,
                                                                                  'book_count': book.book_count,
                                                                                  'is_available': book.book_count > 0}}),
                                 200)
        return make_response(jsonify({'message': 'user not found.'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while fetching book.'}), 500)


@app.route('/books', methods=['GET'])
def get_all_books():
    try:
        books = Book.query.all()
        return make_response(jsonify({'message': 'All Books are successfully fetched!', 'Book': [{'name': book.name,
                                                                                                  'author': book.author,
                                                                                                  'description': book.description,
                                                                                                  'book_count': book.book_count}
                                                                                                 for book in books]}),
                             200)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while fetching books.'}), 500)


@app.route('/book/increase/<int:book_id>', methods=['PUT'])
def increase_book_count(book_id):
    try:
        quantity = request.json.get('quantity', 1)
        book = Book.query.get(book_id)
        if book is None:
            return {"error": "Book not found"}, 404

        book.book_count += quantity
        db.session.commit()
        return make_response(jsonify({'message': 'Book returned successfully!'}), 200)

    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while returning book.'}), 500)


@app.route('/book/decrease/<int:book_id>', methods=['PUT'])
def decrease_book_count(book_id):
    try:
        quantity = request.json.get('quantity', 1)
        book = Book.query.get(book_id)
        if book is None:
            return {"error": "Book not found"}, 404

        if book.book_count < quantity:
            return {"error": "Not enough books in stock"}, 400

        book.book_count -= quantity
        db.session.commit()
        return make_response(jsonify({'message': 'Book issues successfully!'}), 200)

    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while issuing book.'}), 500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
