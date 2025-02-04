from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        operation = request.form['operation']

        # Handle different operations
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            result = a / b if b != 0 else 'Error: Division by zero'
        elif operation == 'modulus':
            result = a % b if b != 0 else 'Error: Modulus by zero'
        else:
            result = 'Error: Invalid operation'
    except ValueError:
        result = 'Error: Invalid input'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
