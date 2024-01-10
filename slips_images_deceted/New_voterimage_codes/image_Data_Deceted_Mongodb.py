import os
import cv2
import pytesseract
from pymongo import MongoClient

folder_path = r'C:\Users\vivif\PycharmProjects\Single_slip_images_Deceted\large_boxes'

# Creation of MongoClient
client = MongoClient()

import urllib.parse

client = MongoClient('mongodb://localhost:27017/')

# Access database
mydatabase = client['Data_conversion3']

# Access collection of the database
mycollection = mydatabase['2024_dummy_data_Voter_slip_data2']
myimage = mydatabase['test2']

# Dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is a NoSQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main_convert(x, y, w, h, im2, img_file=None):
    # print(h)
    width = int(w / 3)
    im2 = cv2.imread(im2)
    f = open('test.txt', 'a')
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 255), 4)
    cropped = im2[y:y + h, x:x + w]
    img = cv2.resize(rect, (1020, 750))
    cv2.imshow('d', img)
    cv2.waitKey(3)
    text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
    f = open('../sample.txt', 'w')
    f.write(text)
    f.close()


l = os.listdir(folder_path)
for i in l:
    file = i
    print(file)
    main_convert(4, 5, 1235, 470, im2=f"{folder_path}\{i}")
    f = open('../sample.txt', 'r')
    x = f.readlines()
    dic = {'voter_slip': file, 'voter_id': x[0].strip()}  # Rearrange the order of fields
    for jj in x:
        if "Father's Name" in jj:
            dic["Father's Name"] = jj.replace("Father's Name", '').replace(':', '').strip()
            print(jj)
        elif "Husband's Name" in jj:
            dic["Husband's Name"] = jj.replace("Husband's Name", '').replace(':', '').replace('-', '').strip()
            print(jj)
        elif "Name" in jj:
            dic['Name'] = jj.replace('Name', '').replace(":", "").strip()
            print(jj)
        elif "House Number" in jj:
            dic['House Number'] = jj.replace('House Number', '').replace(':', '').strip().replace('Photo is', '')
            print(jj)
        elif "Age:" in jj:
            dic['Age'] = jj.replace('Age:', '').split()[0].strip()
            print(jj)
            dic['Gender'] = jj.replace('Age:', '').split()[2].strip()
            print(jj)

    rec = mycollection.insert_one(dic)




# import os
# import cv2
# import pytesseract
# from pymongo import MongoClient
#
# folder_path = r'C:\Users\vivif\PycharmProjects\Single_slip_images_Deceted\2024_dummy'
#
# # Creation of MongoClient
# client = MongoClient()
#
# import urllib.parse
#
# client = MongoClient('mongodb://localhost:27017/')
#
# # Access database
# mydatabase = client['Data_conversion3']
#
# # Access collection of the database
# mycollection = mydatabase['2024_dummy_data_Voter_slip_data']
# myimage = mydatabase['test2']
#
# # Dictionary to be added in the database
# rec = {
#     'title': 'MongoDB and Python',
#     'description': 'MongoDB is a NoSQL database',
#     'tags': ['mongodb', 'database', 'NoSQL'],
#     'viewers': 104
# }
#
# poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
#
# def main_convert(x, y, w, h, im2, img_file=None):
#     # print(h)
#     width = int(w / 3)
#     im2 = cv2.imread(im2)
#     f = open('test.txt', 'a')
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 255), 4)
#     cropped = im2[y:y + h, x:x + w]
#     img = cv2.resize(rect, (1020, 750))
#     cv2.imshow('d', img)
#     cv2.waitKey(3)
#     text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
#     f = open('sample.txt', 'w')
#     f.write(text)
#     f.close()
#
#
# l = os.listdir(folder_path)
# for i in l:
#     file = i
#     print(file)
#     main_convert(4, 5, 2400, 1500, im2=f"{folder_path}\{i}")
#     f = open('sample.txt', 'r')
#     x = f.readlines()
#     dic = {'voter_slip': file, 'voter_id': x[0].strip()}  # Rearrange the order of fields
#     for jj in x:
#         if "Father's Name" in jj:
#             dic["Father’s Name"] = jj.replace("Father’s Name", '').replace(':', '').strip()
#             print(jj)
#         elif "Husband's Name" in jj:
#             dic["Husband's Name"] = jj.replace("Husband's Name", '').replace(':', '').replace('-', '').strip()
#             print(jj)
#         elif "Name" in jj:
#             dic['Name'] = jj.replace('Name', '').replace(":", "").strip()
#             print(jj)
#         elif "House Number" in jj:
#             dic['House Number'] = jj.replace('House Number', '').replace(':', '').strip().replace('Photo is', '')
#             print(jj)
#
#     rec = mycollection.insert_one(dic)
#
#


# import pytesseract
#
# import cv2
# import os
# from pymongo import MongoClient
#
# folder_path = r'C:\Users\vivif\PycharmProjects\Single_slip_images_Deceted\Allslips'
#
# # creation of MongoClient
# client = MongoClient()
# he = []
#
# import urllib.parse
#
# client = MongoClient('mongodb://localhost:27017/')
#
# # Access database
# mydatabase = client['Data_conversion3']
#
# # Access collection of the database
# mycollection = mydatabase['Voter_slip_data']
# myimage = mydatabase['test2']
#
# # dictionary to be added in the database
# rec = {
#     'title': 'MongoDB and Python',
#     'description': 'MongoDB is no SQL database',
#     'tags': ['mongodb', 'database', 'NoSQL'],
#     'viewers': 104
# }
#
# poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
#
# def main_convert(x, y, w, h, im2, img_file=None):
#     print(h)
#     # try:4
#     width = int(w / 3)
#     im2 = cv2.imread(im2)
#     f = open('test.txt', 'a')
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 255), 4)
#     cropped = im2[y:y + h, x:x + w]
#     img = cv2.resize(rect, (1020, 750))
#     cv2.imshow('d', img)
#     cv2.waitKey(3)
#     # count=count+1
#     text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
#     # print(text)
#     f = open('sample.txt', 'w')
#     f.write(text)
#     f.close()
#
#
# l = os.listdir(folder_path)
# for i in l:
#     file = i
#     print(file)
#     main_convert(4, 5, 1235, 470, im2=f"{folder_path}\{i}")
#
#     f = open('sample.txt', 'r')
#     x = f.readlines()
#     dic = {}
#     for i in x:
#         dic['Voter_file_tracker'] = file
#
#         if "Father's Name" in i:
#             dic["Father's Name"] = i.replace("Father's Name", '').replace(':', '')
#             print(i)
#         elif "Husband's Name" in i:
#             dic["Husband's Name"] = i.replace("Husband's Name", '').replace(':', '').replace('-', '')
#             print(i)
#         elif "Name" in i:
#             dic['Name'] = i.replace('Name', '').replace(":", "").replace(' ', '')
#             print(i)
#         elif "House Number" in i:
#             dic['House Number'] = i.replace('House Number', '').replace(' ', '').replace(':', '').replace(' ',
#                                                                                                           '').replace(
#                 'Photo is Available', '').replace('Photois', '')
#             print(i)
#         elif "Age" in i:
#             dic['Age'] = i.replace('Age', '').replace('Gender: FEMALE Photo is', '').replace('Gender: FEMALE',
#                                                                                              '').replace(
#                 'Gender: MALE Photo is', '').replace('Gender: MALE', '').replace('Available', '').replace(":", "")
#             print(i)
#         elif "Gender" in i:
#             dic['Gender'] = i.replace('Gender', '').replace(':', '')
#             print(i)
#
#     rec = mycollection.insert_one(dic)
