# RAJWADA EV KURAWAR - OMAHA Electric Scooter Website

## Requirements
- Python 3.9 or newer
- pip

## Run on Windows
1. Extract this ZIP file.
2. Open the `rajwada_ev_website` folder.
3. Open Command Prompt in this folder.
4. Run:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

5. Open http://127.0.0.1:5000 in your browser.

## Run on macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000.

## Important notes
- Test ride requests are stored in `bookings.db` in this project folder.
- The current product cards use CSS scooter illustrations as temporary placeholders. Replace them with your actual OMAHA scooter photos when available.
- The displayed ₹40,000–₹80,000 price range and 50–150 km range are the dealer-provided overall ranges, not model-specific promises. Confirm exact model-wise details with the showroom.
- Before public deployment, change `app.secret_key` in `app.py`, turn off debug mode, and use a production WSGI server such as Gunicorn or Waitress.
- WhatsApp enquiries open a chat to the showroom number configured in `app.py`.
