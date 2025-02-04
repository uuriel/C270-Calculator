import pytest
from app import app

# Set up a test client using Flask's built-in test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test addition
def test_addition(client):
    response = client.post('/calculate', data={'a': 10, 'b': 5, 'operation': 'add'})
    assert response.status_code == 200
    assert b'10.0 + 5.0 = 15.0' in response.data
    print("✅ Addition Test Passed")

# Test subtraction
def test_subtraction(client):
    response = client.post('/calculate', data={'a': 10, 'b': 5, 'operation': 'subtract'})
    assert response.status_code == 200
    assert b'10.0 - 5.0 = 5.0' in response.data
    print("✅ Subtraction Test Passed")

# Test multiplication
def test_multiplication(client):
    response = client.post('/calculate', data={'a': 10, 'b': 5, 'operation': 'multiply'})
    assert response.status_code == 200
    assert b'10.0 * 5.0 = 50.0' in response.data
    print("✅ Multiplication Test Passed")

# Test division
def test_division(client):
    response = client.post('/calculate', data={'a': 10, 'b': 5, 'operation': 'divide'})
    assert response.status_code == 200
    assert b'10.0 / 5.0 = 2.0' in response.data
    print("✅ Division Test Passed")

# Test division by zero
def test_divide_by_zero(client):
    response = client.post('/calculate', data={'a': 10, 'b': 0, 'operation': 'divide'})
    assert response.status_code == 200
    assert b'Cannot divide by zero.' in response.data
    print("✅ Division by Zero Test Passed")

# Test modulus operation
def test_modulus(client):
    response = client.post('/calculate', data={'a': 10, 'b': 3, 'operation': 'modulus'})
    assert response.status_code == 200
    assert b'10.0 % 3.0 = 1.0' in response.data
    print("✅ Modulus Test Passed")

# Test modulus by zero
def test_modulus_by_zero(client):
    response = client.post('/calculate', data={'a': 10, 'b': 0, 'operation': 'modulus'})
    assert response.status_code == 200
    assert b'Cannot perform modulus by zero.' in response.data
    print("✅ Modulus by Zero Test Passed")

# Test invalid operation
def test_invalid_operation(client):
    response = client.post('/calculate', data={'a': 10, 'b': 5, 'operation': 'invalid'})
    assert response.status_code == 200
    assert b'Invalid operation' in response.data
    print("✅ Invalid Operation Test Passed")

# Test invalid input
def test_invalid_input(client):
    response = client.post('/calculate', data={'a': 'abc', 'b': 5, 'operation': 'add'})
    assert response.status_code == 200
    assert b'Error' in response.data
    print("✅ Invalid Input Test Passed")
