
import pytesseract

import cv2
import os
from pymongo import MongoClient

folder_path = r'C:\Users\vivif\Desktop\inside2'

# creation of MongoClient
client = MongoClient()
he = []

import urllib.parse

client = MongoClient('mongodb://localhost:27017/')

# Access database
mydatabase = client['Data_conversion3']

# Access collection of the database
mycollection = mydatabase['Voter_slip_data3']
myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main_convert(x, y, w, h, im2, img_file=None):
    print(h)
    # try:4
    width = int(w / 3)
    im2 = cv2.imread(im2)
    f = open('test.txt', 'a')
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 255), 4)
    cropped = im2[y:y + h, x:x + w]
    img = cv2.resize(rect, (1020, 750))
    cv2.imshow('d', img)
    cv2.waitKey(3)
    # count=count+1
    text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
    # print(text)
    f = open('../sample.txt', 'w')
    f.write(text)
    f.close()


l = os.listdir(folder_path)
for i in l:
    file = i
    print(file)
    main_convert(2, 2, 1900, 300, im2=f"{folder_path}\{i}")

    f = open('../sample.txt', 'r')
    x = f.readlines()
    dic = {}
    dic = {'voter_slip': file}  # Rearrange the order of fields
    for jj in x:
        if "Assembly Constituency No and Name" in jj:
            dic["Assembly Constituency No and Name"] = jj.replace("Assembly Constituency No and Name", '').replace(':', '').strip()
            print(jj)
        elif "Section No and Name" in jj:
            dic["Section No and Name"] = jj.replace("Section No and Name", '').replace(':', '').replace('-', '').strip()
            print(jj)
    rec = mycollection.insert_one(dic)

