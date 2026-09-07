# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI. Practice defining routes, accepting request data, returning JSON responses, and using HTTP status codes to create a practical web service.

## 📝 Tasks

### 🛠️ Create API Routes

#### Description

Set up the FastAPI application and create routes for viewing the service status and retrieving a list of books.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Add a `GET /` route that returns a welcome message.
- Add a `GET /books` route that returns the provided books as JSON.
- Return consistent JSON object or list responses from each route.

### 🛠️ Add a Book Endpoint

#### Description

Create an endpoint that accepts a new book and adds it to the in-memory collection. Use a Pydantic model to validate the request body.

#### Requirements

Completed program should:

- Define a `Book` model with a title and author.
- Add a `POST /books` route that accepts a validated `Book` request body.
- Add the new book to the in-memory books collection.
- Return the created book with an appropriate success response.

### 🛠️ Retrieve a Book by ID

#### Description

Add a route with a path parameter so users can request one book by its ID. Handle requests for IDs that do not exist.

#### Requirements

Completed program should:

- Add a `GET /books/{book_id}` route with an integer path parameter.
- Return the matching book when the ID exists.
- Return HTTP status code `404` with a helpful error message when the ID does not exist.
- Test the routes using the FastAPI interactive documentation at `/docs` or an HTTP client.
