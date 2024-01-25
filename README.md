
Library Backend

Library Backend is a Django Rest Framework (DRF) project designed to manage authors, books, and genres. It provides APIs for CRUD operations on authors and books, authentication using tokens, and exporting book data for specific genres.


Features

    Author Management: APIs to create, read, update, and delete authors.
    Book Management: APIs to add, edit, and delete books associated with authors.
    Genre Management: APIs to manage book genres.
    Authentication: Token-based authentication for users.
    Export Books: API endpoint to export book data for a specific genre in CSV or JSON format.
    Admin Interface: Built-in Django admin interface for managing authors, books, and genres.

Technologies Used

    Django: A high-level Python web framework for rapid development.
    Django Rest Framework (DRF): A powerful toolkit for building Web APIs in Django.
    SQLite: A lightweight and easy-to-use database engine.

Installation

    To get started, clone this repository to your local machine:

git clone https://github.com/rahul2800/library-system-DRF.git

cd ttofl

    Create a virtual environment and install the dependencies:

python -m venv env

source venv/bin/activate # On Windows use venv\Scripts\activate

pip install -r requirements.txt
Usage

Run python manage.py migrate

Run python manage.py runserver

This will start the server on http://localhost:8000/. You can access the API documentation by visiting http://localhost:8000/api/

login logout for author and admin 
admin credential use 

http://localhost:8000/api/login

http://localhost:8000/api/logout/

API Endpoints

    Authors: /api/authors/
    Genres: /api/genres/
    Books: /api/books/
    Export Books for Genre: /api/export-books/{genre_id}/

For detailed API documentation, refer to the API documentation (to be updated).
Authentication

    Login: /api/login/
    Logout: /api/logout/

Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

