import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase Admin SDK if it's not already initialized
if not firebase_admin._apps:
    # Initialize Firebase Admin with your credentials
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://facerecognition-8afb8-default-rtdb.firebaseio.com/',
        'storageBucket': 'facerecognition-8afb8.appspot.com'
    })

# Access the storage bucket
bucket = storage.bucket('facerecognition-8afb8.appspot.com')

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
















