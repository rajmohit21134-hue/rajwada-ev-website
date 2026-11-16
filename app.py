from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-deployment"
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "bookings.db"

SHOWROOM = {
    "name": "RAJWADA EV KURAWAR",
    "brand": "OMAHA",
    "address": "Raj Traders, Talen Road, Kurawar Mandi",
    "phone_display": "8103577234",
    "phone_whatsapp": "918103577234",
    "email": "rajmohit21134@gmail.com",
}

MODELS = [
    "Starling Neo", "Tezo", "Tezo GT", "Drake 3 Wheel",
    "Loader 2 Tyre", "Dash Plus", "Canary", "Chetak",
    "Single Light", "Double Light"
]

def init_db():
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS test_ride_bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                model TEXT NOT NULL,
                preferred_date TEXT,
                message TEXT,
                created_at TEXT NOT NULL
            )
        """)
        con.commit()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        customer_name = request.form.get("customer_name", "").strip()
        phone = request.form.get("phone", "").strip()
        model = request.form.get("model", "").strip()
        preferred_date = request.form.get("preferred_date", "").strip()
        message = request.form.get("message", "").strip()

        if not customer_name or not phone or model not in MODELS:
            flash("Please enter your name, phone number and select a scooter model.", "error")
            return redirect(url_for("home") + "#test-ride")

        with sqlite3.connect(DB_PATH) as con:
            con.execute("""
                INSERT INTO test_ride_bookings
                (customer_name, phone, model, preferred_date, message, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (customer_name, phone, model, preferred_date, message,
                  datetime.now().isoformat(timespec="seconds")))
            con.commit()

        flash("Thank you! Your test ride request has been received. Our showroom will contact you.", "success")
        return redirect(url_for("home") + "#test-ride")

    return render_template("index.html", showroom=SHOWROOM, models=MODELS)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
