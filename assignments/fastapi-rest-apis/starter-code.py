"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    """A book that can be added to the collection."""

    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


# TODO: Add a GET / route that returns a welcome message.


# TODO: Add a GET /books route that returns all books.


# TODO: Add a POST /books route that accepts a Book and adds it to the collection.


# TODO: Add a GET /books/{book_id} route.
# Raise HTTPException(status_code=404, detail="Book not found") when needed.


# Run with:
# uvicorn starter-code:app --reload
