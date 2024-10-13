import cv2
import dlib
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase (replace with your own Firebase credentials)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecogition-21440-default-rtdb.firebaseio.com/",})


with open('EncodeFile.p', 'rb') as file:
    known_face_encodings, known_face_names = pickle.load(file)


video_capture = cv2.VideoCapture(0)

while True:
   
    ret, frame = video_capture.read()

   
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "None"  

        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            
            user_ref = db.reference('person/' + name)
            user_data = user_ref.get()
            print("id:", name)
            print("the data of person:", user_data)
           
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    
    cv2.imshow('Video', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
