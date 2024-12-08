Library Management System
Overview

This is a Library Management System built with Django and Django REST Framework. It allows users to manage books, including adding, deleting, searching, and updating book details via a REST API.

Features:

**-Add**

**-Delete**

**-Search**

**-Display**

**-Change** the status of a book (e.g., "in stock" or "issued").


**Docker Setup:**

Build the Docker Image:

    docker build -t library-management .

Run the Docker Container:

    docker run -p 8000:8000 library-management

(This will start the server on port 8000.
Open your browser and go to http://127.0.0.1:8000/ to access the API)


API Endpoints

    GET /library/books/: Fetch all books.
    POST /library/books/: Add a new book.
    GET /library/books/{id}/: Fetch a book by ID.
    PUT /library/books/{id}/: Update the status of a book.
    DELETE /library/books/{id}/: Delete a book.
