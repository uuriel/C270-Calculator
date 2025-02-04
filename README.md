import requests

# Define the URL of the Flask app
url = "http://localhost:3000/calculate"

# Define the test data
data = {
    'a': 15,
    'b': 4,
    'operation': 'modulus'
}

# Send a POST request to the Flask app
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    
    # Check if the result is as expected
    if result['result'] == 3.0:
        print("✅ Modulus Test Passed")
    else:
        print(f"❌ Modulus Test Failed: Expected 3.0, got {result['result']}")
else:
    print(f"❌ Request Failed: Status Code {response.status_code}")
