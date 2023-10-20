from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from .models import *
from .serializer import UploadimageSerializer
from django.http import HttpResponse
from rest_framework import status

from rest_framework.parsers import MultiPartParser


@parser_classes((MultiPartParser,))
class Uploadimage(generics.GenericAPIView):
    serializer_class = UploadimageSerializer

    def post(self, request):
        a = UploadimageSerializer(data=request.data)
        a.is_valid(raise_exception=True)
        a.save()
        return Response("upload success")









import pytesseract

import cv2
import os
from pymongo import MongoClient


folder_path = r'C:\Users\vivif\Desktop\dummy1'

# creation of MongoClient
client = MongoClient()
he = []

import urllib.parse

Username = 'devops_admin'
Password = 'Devops1234'
username = urllib.parse.quote_plus(Username)
password = urllib.parse.quote_plus(Password)
# Connect with the portnumber and host
client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('mongodb://%s:%s@13.234.70.44:27017' % (username,password))

# Access database
mydatabase = client['Data_conversion3']

# Access collection of the database
mycollection = mydatabase['jagan']
# myimage = mydatabase['test2']

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
    # print(h)
    # try:4
    width = int(w / 3)
    im2 = cv2.imread(im2)
    f = open('test.txt', 'a')
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cropped = im2[y:y + h, x:x + w]
    img = cv2.resize(rect, (1020, 750))
    cv2.imshow('d', img)
    cv2.waitKey(1)
    # count=count+1
    text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
    # print(text)
    f = open('sample.txt', 'w')
    f.write(text)
    f.close()


# image_path = r'C:\Users\vivif\pythonProject\pythonProject3\SAMPLE'
l = os.listdir(folder_path)
for i in l:
    file = i
    # print(file)
    main_convert(5, 5, 1240, 450, im2=f"{folder_path}\{i}")

    f = open('sample.txt', 'r')
    x = f.readlines()
    dic = {}
    voterID = x[0]

    for i in x:
        dic['Voter_file_tracker'] = file
        dic['Voter_id'] = voterID
        # print(voterID)
        # print(i[0:10])
        if i.startswith('Name'):
            # if "Name" in i:
            Name = i.replace('Name', '').replace(':', '').replace(' ', '').replace('-', '').strip()
            dic['Name'] = Name
            print('Name',Name)

        if i.startswith("Father's Name"):

            father_name = i.replace("Father's Name", '').replace(':', '').replace(' ', '').replace('-',
                                                                                                            '').strip()
            dic["Father's Name"] = father_name
            print(father_name)


        elif i.startswith("Husband's Name"):
            husband_name = i.replace("Husband's Name", '').replace(':', '').replace(' ', '').replace('-','').strip()
            dic["Husband's Name"] = husband_name
            print(husband_name)


        elif i.startswith("Mother's Name"):
            Mother_Name = i.replace("Mother's Name", '').replace(':', '').replace(' ', '').replace('-',
                                                                                                            '').strip()
            dic["Mother's Name"] = Mother_Name
            print(Mother_Name)


        elif i.startswith("House Number"):
            House_Number = i.replace("House Number", '').replace(':', '').replace(' ', '').replace(';',
                                                                                                          '').strip()
            dic['House Number'] = House_Number
            print(House_Number)

        elif i.startswith("Age"):
            age = str(i)[5:7]
            print(age)
            gender = str(i)[16:22]
            print(gender)

            dic["Age"] = age
            dic["Gender"] = gender
            print(voterID)
            rec = mycollection.insert_one(dic)