from pymongo import MongoClient

# creation of MongoClient
client = MongoClient()


import urllib.parse

# Connect with the portnumber and host
client = MongoClient('mongodb://localhost:27017/')

# Access database
mydatabase = client['Data_conversion987']

# Access collection of the database
mycollection = mydatabase['Anakapalli19']
# myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

fan = {                                             #this is a set name your choosing

    "Name":"Jagadeeshm",
    "company": "vivify health care solutions",
    "phone": "1234567891",
    "employe id": "14363",
    "Hr madam": "Hema,Swathi,Roja"
}

rec = mycollection.insert_one(fan)