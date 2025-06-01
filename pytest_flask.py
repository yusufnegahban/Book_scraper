import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Book List" in rv.data

def test_search_books(client):
    rv = client.get("/?search=python")
    assert rv.status_code == 200

def test_book_detail(client):
    rv = client.get("/book/1")
    assert rv.status_code in [200, 404]

def test_api_books(client):
    rv = client.get("/api/books")
    assert rv.status_code == 200
    assert "books" in rv.get_json()

def test_api_book_detail(client):
    rv = client.get("/api/book/1")
    if rv.status_code == 200:
        data = rv.get_json()
        assert "title" in data
    else:
        assert rv.status_code == 404

