import MySQLdb.cursors
from flask import Flask, render_template, redirect, request, session, url_for
import mysql.connector
import json


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
                    session['loginsuccess'] = True
                    return render_template('bookingpage.html')
            else:
                render_template('login.html')

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
    # if session['loginsuccess']:
    if request.method == "POST":
        if 'departure-city' in request.form and "arrival-city" in request.form and 'adult-quantity' in request.form\
                and 'children-quantity' in request.form and 'flight-class' in request.form:

            departure_location = request.form['departure-city']
            arrival_location = request.form['arrival-city']
            session['adult_quantity'] = request.form['adult-quantity']
            session['children_quantity'] = request.form['children-quantity']
            session['flight_class'] = request.form['flight-class']
            print(departure_location)
            print(arrival_location)


            cursor = db_flights.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM flightsdb.flights WHERE departure_city= %s AND arrival_city =%s",
                           (departure_location, arrival_location))
            info = cursor.fetchall()
            if info:
                return render_template('flights_view.html', info=info)
                # return redirect(url_for('view_flights'), info=info)

    return render_template("bookingpage.html")


@app.route('/flights', methods=['GET', 'POST'])
def view_flights():

    return render_template("flights_view.html")


@app.route('/postmethod', methods= ['POST'])
def get_post_javascript_data():
    jsdata = request.get_json
    print(jsdata)
    print(type(jsdata))
    results = json.loads(jsdata)
    print(results)
    print(type(results))

    return results


@app.route('/pricing', methods=['GET', 'POST'])
def pricing():
    print(session['adult_quantity'])
    print(session['children_quantity'])
    print(session['flight_class'])

    return render_template("pricing.html")


if __name__ == '__main__':
    app.run(debug=True)




# post method is used to get the the form data.
# get method retrieves the information from the server

# method to retrieve info from HTML
# form = cgi.FieldStorage()
# trip_way = form.getvalue('check')
# departure_location = form.getvalue('departure-city')


# departure_date = request.form['depart-date']
#             return_date = request.form['return-date']
#
# trip_way = request.form['check']
