
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if not firebase_admin._apps:
    cred = credentials.Certificate('serviceAccountKey.json') 
    default_app = firebase_admin.initialize_app(cred, {

    'databaseURL': "https://facerecognition-8afb8-default-rtdb.firebaseio.com/"
    
})
ref = db.reference('Students')

data = {
    "021":
        {
            "name": "Geeta",
            "major": "IT",
            "starting_year": 2023,
            "total_attendance": 9,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-04-11 00:54:34"
        },
    
    "047":
        {
            "name": "Pooja",
            "major": "IT",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-04-11 00:54:34"
        },
    "048":
        {
            "name": "Elon Musk",
            "major": "IT",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)