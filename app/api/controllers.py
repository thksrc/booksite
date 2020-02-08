from flask import Blueprint, jsonify
from app.models import Book

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/<isbn>", methods=["GET"])
def api(isbn):
    book = Book.query.filter_by(isbn=isbn).first()

    if book is None:
        return jsonify({'Error': 'Invalid book ISBN'}), 422

    review_count = len(book.reviews)
    
    if review_count == 0:
        average_score = 0
    else:
        average_score = 0
        for review in book.reviews:
            average_score += review.rating
        average_score /= float(review_count)

    data = {
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'isbn': book.isbn,
        'review_count': review_count,
        'average_score': average_score
    }

    return jsonify(data)