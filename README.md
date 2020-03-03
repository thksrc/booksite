# Booksite

*Booksite is a book reviews site implemented using the micro framework Flask, SQLAlchemy, the Goodreads API, Tailwind CSS, and Heroku for deployment.*

This project is heavily based off of the CS50 web development course project 1, which can be found [here](https://docs.cs50.net/ocw/web/projects/1/project1.html). I changed a lot of the original requirements and implemented things according to how a full flask application would be like. As such, I use features like Blueprints to seperate different parts of the application, and I seperate all of my front end code.

## Features

 - **Login and Register**

Users are required to login and register to access the book review functionality of the website. There is a page for registering and logging in. There is also authentication, where if a field is not filled out, or a username is taken, then it returns the same page with an error message. For registration, the data is stored in a SQLAlchemy database, where passwords are set using werkzeug, for security.

 - **Search for books**
 
This is the page that users are brought to when they first login or register. The search works as you would think it would work, returning a list of books after typing in a term and submitting. The terms can be either the ISBN number, the author, or the name of the book. The querying is done via the SQLAclehym ORM.

 - **Book page/Goodreads API and Reviews**

After searching and clicking on a book, users are brought to a book page. There are two main parts to this page, the book info and the reviews. The book info contains the book name, the author, the ISBN number, as well as data requested from the Goodreads API to show the average rating on Goodreads, and the number of reviews on Goodreads. The reviews section underneath this contains a list of the already present reviews, if there are any. Using SQLAlchemy relationships, there are the names of the users that submitted the reviews displayed, and each review will only correspond with one book. Users can submit reviews through a form, which includes a message, as well as a rating from 1 to 5 that they can choose from. After submitting a review, users are immediately redirected to the same book page, where their review should show up along with any other reviews.

 - **API access**
 
Submitting a GET request to /api/&lt;isbn> will return a JSON object with information including the name of the book, the number of reviews submitted through this website, and the average rating. This is useful for other websites looking to get data submitted through this website.

> Note that this repository is mostly for my learning and others learning, so the website is just for example and will most likely not actually be used.

## License

[MIT](https://github.com/thksrc/booksite/blob/master/LICENSE)
