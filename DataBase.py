import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,{'databaseURL':"https://facerecogition-21440-default-rtdb.firebaseio.com/"
})

ref = db.reference('person')

data = {
    "1113713737": {
        "name": "abdulmalik faden",
        "gender": "male",
        "company mobile": 966562364481,
        "addres": "hotel:dar almqam",
        "age": 22,
        "Nationality" : "saudi" , 
        "last_seen_time":"2023-12-3 00:48:20"
        
    },
    "1118323615": {
        "name": "abdulmajed alzhrani",
        "gender": "male",
        "company mobile": 966562364481,
        "addres": "hotel:dar almqam",
        "age": 21,
        "Nationality" : "bangladish" ,
        "last_seen_time":"2023-12-10 11:20:00"
    },
    "1114532180": {
        "name": "alwaled faden",
        "gender": "male",
        "company mobile": 966562364481,
        "addres": "hotel:alrwdah",
        "age": 21,
        "Nationality" : "indinesia" ,
        "last_seen_time":"2023-12-09 01:01:00"
    },
    "1112532840": {
        "name": "yhya bazeed",
        "gender": "male",
        "company mobile": 966562364481,
        "addres": "hotel:alrwdah",
        "age": 21,
        "Nationality" : "india" , 
        "last_seen_time":"2023-12-05 04:41:50"
    }
}


for key,value in data.items():
    ref.child(key).set(value)
