from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('doctor.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']
    gender = request.form['gender']


    return render_template('confirmation.html', name=name, date=date, time=time ,gender=gender)

if __name__ == '__main__':
    app.run(debug=True)
