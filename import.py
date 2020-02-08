from app import create_app
from app import db
from app.models import Book
import os
import csv

app = create_app()

basedir = os.path.abspath(os.path.dirname(__file__))

file = open(os.path.join(basedir, "books.csv"))
reader = csv.reader(file)

next(reader)

for isbn, title, author, year in reader:
    with app.app_context():
        book = Book(isbn=isbn,
                    title=title,
                    author=author,
                    year=int(year))
        db.session.add(book)
        db.session.commit()

    print(f"Added book {title} to db")