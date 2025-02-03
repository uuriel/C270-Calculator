from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = request.form.get('a', type=float)
    b = request.form.get('b', type=float)
    operation = request.form.get('operation')
    result = None
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
