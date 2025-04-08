from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production

DATABASE = 'applications.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            firstName TEXT,
            surname TEXT,
            parentPhone TEXT,
            grade TEXT,
            school TEXT,
            packageHours INTEGER,
            packagePrice INTEGER,
            scheduleData TEXT,
            startDay TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form fields
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        surname = request.form.get('surname')
        parentPhone = request.form.get('parentPhone')
        grade = request.form.get('grade')
        school = request.form.get('school')
        packageHours = request.form.get('selectedPackageHours')
        packagePrice = request.form.get('selectedPackagePrice')
        scheduleData = request.form.get('scheduleData')  # This is a JSON string
        startDay = request.form.get('startDay')

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''
            INSERT INTO applications 
            (email, firstName, surname, parentPhone, grade, school, packageHours, packagePrice, scheduleData, startDay)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (email, firstName, surname, parentPhone, grade, school, packageHours, packagePrice, scheduleData, startDay))
        conn.commit()
        conn.close()

        flash("Application submitted successfully!")
        # Redirect to the payment page after successful submission
        return redirect(url_for('payment'))
    return render_template('index.html')

@app.route('/payment', methods=['GET'])
def payment():
    # Render the payment page where Yoco integration occurs.
    return render_template('payment.html')

@app.route('/thankyou', methods=['GET'])
def thankyou():
    # Simple thank-you page after payment.
    return "<h2>Thank you for your payment!</h2>"

@app.route('/admin', methods=['GET'])
def admin():
    # Retrieve search query from the URL (if provided)
    search_query = request.args.get('search', '').strip()
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    if search_query:
        query = """
            SELECT id, email, firstName, surname, parentPhone, grade, school, packageHours, packagePrice, scheduleData, startDay 
            FROM applications 
            WHERE firstName LIKE ? OR surname LIKE ? OR parentPhone LIKE ?
            ORDER BY id DESC
        """
        like_query = f"%{search_query}%"
        c.execute(query, (like_query, like_query, like_query))
    else:
        c.execute("""
            SELECT id, email, firstName, surname, parentPhone, grade, school, packageHours, packagePrice, scheduleData, startDay 
            FROM applications ORDER BY id DESC
        """)
    records = c.fetchall()
    conn.close()
    return render_template('admin.html', records=records, search_query=search_query)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
