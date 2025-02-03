from flask import Flask, request, render_template

app = Flask(__name__)

# In-memory storage for calculations
calculations = []

@app.route('/')
def home():
    # Pass the calculations list to the template to display history
    return render_template('index.html', history=calculations)

@app.route('/calculate', methods=['POST'])
def calculate():
    a = request.form.get('a', type=float)
    b = request.form.get('b', type=float)
    operation = request.form.get('operation')
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
    # Store the calculation in history
    calculations.append(operation_str)
    return render_template('index.html', result=result, history=calculations)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
