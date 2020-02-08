from flask import Blueprint, render_template, session, redirect, url_for, request
import requests
import os
from app import db
from app.models import Book, Review

main_bp = Blueprint("main", __name__)

@main_bp.route("/") 
def home():
    if session.get('logged_in') is True:
        return render_template("main/home.html", homepage=True)
    else:
        return redirect(url_for('account.login'), "403")

@main_bp.route("/search", methods=["GET"])
def search():
    if session.get('logged_in') is True:
        if not request.args.get("book"):
            return render_template("main/home.html", homepage=True, error="No Search")
        search = request.args.get("book")
        query = "%{}%".format(search)
        books = Book.query.filter(Book.isbn.like(query) | Book.title.like(query) | Book.author.like(query)).limit(15).all()
        return render_template("main/results.html", title="Search", books=books)
    else:
        return redirect(url_for('main.home'))

@main_bp.route("/book/<isbn>", methods=["GET", "POST"])
def book(isbn):
    if session.get('logged_in') is True:
        if request.method == "GET":
            book_info = Book.query.filter_by(isbn=isbn).first().__dict__
            del book_info['_sa_instance_state']

            res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": os.getenv("GOODREADS_KEY"), "isbns": isbn}).json()
            goodreads_data = res['books'][0]
            book_info.update(goodreads_data)

            reviews = Book.query.filter_by(isbn=isbn).first().reviews

            return render_template("main/book.html", title=book_info['title'], book_info=book_info, reviews=reviews)
        else:
            comment = request.form.get("comment")
            rating = request.form.get("rating")
            user_id = session['user_id']
            review = Review(user_id=user_id,
                            book_isbn=isbn,
                            comment=comment,
                            rating=int(rating))
            db.session.add(review)
            db.session.commit()
            return redirect(url_for('main.book', isbn=isbn))
    else:
        return redirect(url_for('main.home'))