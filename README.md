import requests

# Define the URL of the Flask app
url = "http://localhost:3000/calculate"

# Define a helper function to send POST requests
def send_calculation_request(a, b, operation):
    data = {
        'a': a,
        'b': b,
        'operation': operation
    }
    return requests.post(url, data=data)

# Define the test cases
def test_addition():
    response = send_calculation_request(10, 5, 'add')
    assert response.status_code == 200
    assert response.json()['result'] == 15.0
    print("✅ Addition Test Passed")

def test_subtraction():
    response = send_calculation_request(10, 5, 'subtract')
    assert response.status_code == 200
    assert response.json()['result'] == 5.0
    print("✅ Subtraction Test Passed")

def test_multiplication():
    response = send_calculation_request(10, 5, 'multiply')
    assert response.status_code == 200
    assert response.json()['result'] == 50.0
    print("✅ Multiplication Test Passed")

def test_division():
    response = send_calculation_request(10, 5, 'divide')
    assert response.status_code == 200
    assert response.json()['result'] == 2.0
    print("✅ Division Test Passed")

def test_divide_by_zero():
    response = send_calculation_request(10, 0, 'divide')
    assert response.status_code == 200
    assert response.json()['result'] == "Cannot divide by zero."
    print("✅ Division by Zero Test Passed")

def test_modulus():
    response = send_calculation_request(10, 3, 'modulus')
    assert response.status_code == 200
    assert response.json()['result'] == 1.0
    print("✅ Modulus Test Passed")

def test_modulus_by_zero():
    response = send_calculation_request(10, 0, 'modulus')
    assert response.status_code == 200
    assert response.json()['result'] == "Cannot perform modulus by zero."
    print("✅ Modulus by Zero Test Passed")

def test_invalid_operation():
    response = send_calculation_request(10, 5, 'invalid')
    assert response.status_code == 200
    assert response.json()['result'] == "Invalid operation"
    print("✅ Invalid Operation Test Passed")

def test_invalid_input():
    response = send_calculation_request("abc", 5, 'add')
    assert response.status_code == 200
    assert "Error" in response.json()['result']
    print("✅ Invalid Input Test Passed")

# Run all tests
if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_divide_by_zero()
    test_modulus()
    test_modulus_by_zero()
    test_invalid_operation()
    test_invalid_input()

