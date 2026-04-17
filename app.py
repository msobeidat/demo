from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    num1 = ""
    num2 = ""
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        if num1 and num2:
            result = int(num1) + int(num2)
    return render_template('index.html', result=result, num1=num1, num2=num2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) # nosec
