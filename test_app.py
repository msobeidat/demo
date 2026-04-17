import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """تأكد أن الصفحة الرئيسية تعمل وتظهر كلمة Calculator"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Calculator" in rv.data

def test_addition(client):
    """تأكد أن عملية الجمع تعمل من خلال الـ Form"""
    rv = client.post('/', data=dict(num1="10", num2="20"), follow_redirects=True)
    assert b"30" in rv.data
