from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    reviews = db.relationship('Review', backref='user')

    def __repr__(self):
        return f"Id: {self.id} - Username: {self.username}"

class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String(15), primary_key=True)
    title = db.Column(db.String(128), index=True)
    author = db.Column(db.String(64))
    year = db.Column(db.Integer)
    reviews = db.relationship('Review', backref='book')

    def __repr__(self):
        return f"Title: {self.title}"

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_isbn = db.Column(db.String(15), db.ForeignKey('books.isbn'))
    comment = db.Column(db.String(1000))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f"User {self.user_id} reviewed Book {self.book_isbn}"