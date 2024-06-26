import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_posts(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert b'First Post' in response.data
    assert b'Second Post' in response.data

def test_create_post(client):
    new_post = {'title': 'Test Post', 'body': 'Test body', 'userId': 1}
    response = client.post('/posts', json=new_post)
    assert response.status_code == 201
    assert b'Test Post' in response.data
