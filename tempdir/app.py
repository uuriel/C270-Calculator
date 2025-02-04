from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# In-memory storage for calculations
calculations = []

@app.route('/')
def home():
    # Pass the calculations list to the template to display history
    return render_template('index.html', history=calculations)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        a = request.form.get('a', type=float)
        b = request.form.get('b', type=float)
        operation = request.form.get('operation')
        
        # Initialize result and operation_str
        result = None
        operation_str = ""
        
        if operation == 'add':
            result = a + b
            operation_str = f"{a} + {b} = {result}"
        elif operation == 'subtract':
            result = a - b
            operation_str = f"{a} - {b} = {result}"
        elif operation == 'multiply':
            result = a * b
            operation_str = f"{a} * {b} = {result}"
        elif operation == 'divide':
            if b != 0:
                result = a / b
                operation_str = f"{a} / {b} = {result}"
            else:
                result = "Cannot divide by zero."
                operation_str = f"{a} / {b} = {result}"
        elif operation == 'modulus':
            if b != 0:
                result = a % b
                operation_str = f"{a} % {b} = {result}"
            else:
                result = "Cannot perform modulus by zero."
                operation_str = f"{a} % {b} = {result}"
        else:
            result = "Invalid operation"
            operation_str = f"{a} {operation} {b} = {result}"
        
        # Store the calculation in history
        calculations.append(operation_str)

        # Return the result and history as a JSON response
        return jsonify(result=result, history=calculations)
    
    except Exception as e:
        # In case of unexpected errors, return a JSON response with the error
        return jsonify(result=f"Error: {str(e)}", history=calculations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
