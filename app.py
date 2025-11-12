from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(num1, num2, operator):
    try:
        num1 = float(num1) if num1 else 0
        num2 = float(num2) if num2 else 0

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return "Error: Divide by zero!" if num2 == 0 else num1 / num2
        else:
            return "Select an input!"
        



    except ValueError:
        return "Invalid input!"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    num1 = ''
    num2 = ''
    selected_operator = ''
    if request.method == 'POST':
        num1 = request.form.get('num1', '')
        num2 = request.form.get('num2', '')
        selected_operator = request.form.get('operator', '')
        result = calculate(num1, num2, selected_operator)
    return render_template('index.html',
                           result=result,
                           num1=num1,
                           num2=num2,
                           selected_operator=selected_operator)

if __name__ == '__main__':
    app.run(debug=True)
