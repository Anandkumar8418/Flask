from app import app, db  # Import the app and db from your Flask app

# Set up an application context
with app.app_context():
    db.create_all()
    print("Database created successfully!")
