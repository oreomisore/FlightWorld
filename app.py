import MySQLdb.cursors
from flask import Flask, render_template, redirect, request, session, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = '1234567543'
db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Orerules1',
    port='3306',
    database='logindb'

)

db_flights = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Orerules1',
    port='3306',
    database='flightsdb'

)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'Username' in request.form and 'Password' in request.form:
            username = request.form['Username']
            password = request.form['Password']
            cursor = db.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM logindetails WHERE email = %s AND password=%s", (username, password))
            info = cursor.fetchone()  # whatever values were getting from the cursor is stored as a tuple in the info
            # variable.
            print(info)
            if info is not None:
                if info[2] == username and info[3] == password:
                    # session['loginsuccess'] = True
                    return redirect(url_for('search'))
            else:
                return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/new', methods=['GET', 'POST'])
def new_user():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            name = request.form['one']
            email = request.form['two']
            password = request.form['three']
            cursor = db.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO logindb.logindetails(name, email, password) VALUES(%s, %s, %s)", (name, email,
                                                                                                          password))
            db.commit()
            return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/new/booking', methods=['GET', 'POST'])
def search():
    # if session['loginsuccess'] == True:
    if request.method == "POST":
        if 'departure-city' in request.form and "arrival-city" in request.form and 'adult_quantity' in request.form and \
                'children-quantity' in request.form and 'flight-class' in request.form:

            departure_location = request.form['departure-city']
            arrival_location = request.form['arrival-city']
            adult_quantity = request.form['adult-quantity']
            children_quantity = request.form['children-quantity']
            flight_class = request.form['flight-class']


            cursor = db_flights.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM flightsdb.flights WHERE departure_city= %s AND arrival_city =%s",
                           (departure_location, arrival_location))
            info = cursor.fetchall()
            print(info)
            return render_template('flights_view.html', info=info)

    return render_template("bookingpage.html")


@app.route('/prices', methods=['GET', 'POST'])
def payment(adult_quantity, children_quantity, flight_class):


    return render_template("pricing.html",  )


if __name__ == '__main__':
    app.run(debug=True)


    

