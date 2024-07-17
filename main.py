
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text1 = request.form['textbox1']
    text2 = request.form['textbox2']
    # Here you can perform the desired action with the text box values, 
    # such as saving them to a database or performing calculations.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
