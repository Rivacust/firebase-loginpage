Initialize Firebase Admin SDK:

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)



Setup Pyrebase Config:


import pyrebase

config = {
    "apiKey": "your-api-key",
    "authDomain": "your-project-id.firebaseapp.com",
    "databaseURL": "https://your-database-name.firebaseio.com",
    "projectId": "your-project-id",
    "storageBucket": "your-project-id.appspot.com",
    "messagingSenderId": "your-messaging-sender-id",
    "appId": "your-app-id"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()



Login Code Example


import pyrebase

# Firebase config
config = {
    "apiKey": "your-api-key",
    "authDomain": "your-project-id.firebaseapp.com",
    "databaseURL": "https://your-database-name.firebaseio.com",
    "projectId": "your-project-id",
    "storageBucket": "your-project-id.appspot.com",
    "messagingSenderId": "your-messaging-sender-id",
    "appId": "your-app-id"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Function to log in user
def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in")
        print(f"User ID Token: {user['idToken']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace these with the email and password you want to log in with
email = "user@example.com"
password = "user_password"

login_user(email, password)
