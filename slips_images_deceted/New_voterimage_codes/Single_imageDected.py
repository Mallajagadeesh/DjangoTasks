# import pytesseract
#
# import cv2
# import os
# from pymongo import MongoClient
#
#
# folder_path = r'C:\Users\vivif\Desktop\dummy3'
#
# # creation of MongoClient
# client = MongoClient()
# # he = []
#
#
# # Connect with the portnumber and host
# client = MongoClient('mongodb://localhost:27017/')
# # client = MongoClient('mongodb://%s:%s@13.234.70.44:27017' % (username,password))
#
# # Access database
# mydatabase = client['voterImage']
#
# # Access collection of the database
# mycollection = mydatabase['Single_voter_image']
#
# # myimage = mydatabase['test2']
#
# # dictionary to be added in the database
#
#
# # poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
#
# def main_convert(x, y, w, h, im2, img_file=None):
#     # print(h)
#     # try:4
#     width = int(w / 3)
#     im2 = cv2.imread(im2)
#     f = open('test.txt', 'a')
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
#     cropped = im2[y:y + h, x:x + w]
#     img = cv2.resize(rect, (1020, 750))
#     cv2.imshow('d', img)
#     cv2.waitKey(1)
#     # count=count+1
#     text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
#     # print(text)
#     f = open('sample.txt', 'w')
#     f.write(text)
#     f.close()
#
#
# # image_path = r'C:\Users\vivif\pythonProject\pythonProject3\SAMPLE'
# l = os.listdir(folder_path)
# for i in l:
#     file = i
#     # print(file)
#     main_convert(5, 5, 1240, 450, im2=f"{folder_path}\{i}")
#
#     f = open('sample.txt', 'r')
#     x = f.readlines()
#     dic = {}
#     voterID = x[0]
#
#     for i in x:
#         dic['Voter_file_tracker'] = file
#         dic['Voter_id'] = voterID
#         # print(voterID)
#         # print(i[0:10])
#         if i.startswith('Name'):
#             # if "Name" in i:
#             Name = i.replace('Name', '').replace(':', '').replace(' ', '').replace('-', '').strip()
#             dic['Name'] = Name
#             print('Name',Name)
#
#         if i.startswith("Father's Name"):
#
#             father_name = i.replace("Father's Name", '').replace(':', '').replace(' ', '').replace('-',
#                                                                                                             '').strip()
#             dic["Father's Name"] = father_name
#             print(father_name)
#
#
#         elif i.startswith("Husband's Name"):
#             husband_name = i.replace("Husband's Name", '').replace(':', '').replace(' ', '').replace('-','').strip()
#             dic["Husband's Name"] = husband_name
#             print(husband_name)
#
#
#         elif i.startswith("Mother's Name"):
#             Mother_Name = i.replace("Mother's Name", '').replace(':', '').replace(' ', '').replace('-',
#                                                                                                             '').strip()
#             dic["Mother's Name"] = Mother_Name
#             print(Mother_Name)
#
#
#         elif i.startswith("House Number"):
#             House_Number = i.replace("House Number", '').replace(':', '').replace(' ', '').replace(';',
#                                                                                                           '').strip()
#             dic['House Number'] = House_Number
#             print(House_Number)
#
#         elif i.startswith("Age"):
#             age = str(i)[5:7]
#             print(age)
#             gender = str(i)[16:22]
#             print(gender)
#
#             dic["Age"] = age
#             dic["Gender"] = gender
#             print(voterID)
#             rec = mycollection.insert_one(dic)





# import pytesseract
#
# import cv2
# import os
# from pymongo import MongoClient
#
#
# folder_path = r'C:\Users\vivif\Desktop\dummy3'
#
# # creation of MongoClient
# client = MongoClient()
# # he = []
#
#
# # Connect with the portnumber and host
# client = MongoClient('mongodb://localhost:27017/')
# # client = MongoClient('mongodb://%s:%s@13.234.70.44:27017' % (username,password))
#
# # Access database
# mydatabase = client['voterImage']
#
# # Access collection of the database
# mycollection = mydatabase['Single_voter_image']
#
# # myimage = mydatabase['test2']
#
# # dictionary to be added in the database
#
#
# # poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
#
# def main_convert(x, y, w, h, im2, img_file=None):
#     # print(h)
#     # try:4
#     width = int(w / 3)
#     im2 = cv2.imread(im2)
#     f = open('test.txt', 'a')
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
#     cropped = im2[y:y + h, x:x + w]
#     img = cv2.resize(rect, (1020, 750))
#     cv2.imshow('d', img)
#     cv2.waitKey(1)
#     # count=count+1
#     text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
#     # print(text)
#     f = open('sample.txt', 'w')
#     f.write(text)
#     f.close()
#
#
# # image_path = r'C:\Users\vivif\pythonProject\pythonProject3\SAMPLE'
# l = os.listdir(folder_path)
# # ...
#
# for i in l:
#     file = i
#     # print(file)
#     main_convert(5, 5, 1240, 450, im2=f"{folder_path}\{i}")
#
#     f = open('sample.txt', 'r')
#     x = f.readlines()
#     dic = {}
#     voterID = x[0]
#
#     for i in x:
#         dic['Voter_file_tracker'] = file
#         dic['Voter_id'] = voterID
#
#         # Extract additional name
#         if "Name:" in i:
#             Name = i.split("Name")[1].strip()
#             dic["Name"] = Name
#             print(Name)
#         elif "Husband's Name" in i:
#             name = i.split("Husband's Name")[1]
#             dic["Husband's Name"] = name
#             print(name)
#
#         elif "raju" in i:
#             dic["Husband's Name"] = name[0]
#
#     rec = mycollection.insert_one(dic)





    ######################################### This husband's name double line code ########################################
import pytesseract
import cv2
import os
from pymongo import MongoClient

folder_path = r'C:\Users\vivif\Desktop\dummy3'

# Create a MongoClient
client = MongoClient('mongodb://localhost:27017')

# Access database
mydatabase = client['voterImage']

# Access collection of the database
mycollection = mydatabase['Single_voter_image']

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
    f = open('../sample.txt', 'w')
    f.write(text)
    f.close()


for i in os.listdir(folder_path):
    file = i
    main_convert(5, 5, 1240, 450, im2=f"{folder_path}\{i}")

    f = open('../sample.txt', 'r')
    x = f.readlines()
    dic = {}
    voterID = x[0]
    lastname = x[5]

    for i in x:
        dic['Voter_file_tracker'] = file
        dic['Voter_id'] = voterID
        dic['lastname'] = lastname

        if "Name:" in i:
            Name = i.split("Name")[1].strip()
            dic["Name"] = Name
            print(Name)
        elif "Husband's Name" in i:
            name = i.split("Husband's Name")[1] + lastname
            dic["Husband's Name"] = name
            print(name)
        elif "Wife's Name" in i:
            wife = i.split("Wife's Name")[1] + lastname
            dic["Wife's Name"] = wife
            print(wife)

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

    rec = mycollection.insert_one(dic)


######################################### This Name's and husband's double line code ########################################
# # #
# import pytesseract
# import cv2
# import os
# from pymongo import MongoClient
#
# folder_path = r'C:\Users\vivif\Desktop\Name double lines'
#
# # Create a MongoClient
# client = MongoClient('mongodb://localhost:27017')
#
# # Access database
# mydatabase = client['voterImage']
#
# # Access collection of the database
# mycollection = mydatabase['Single_voter_image']
#
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
#
# def main_convert(x, y, w, h, im2, img_file=None):
#     # print(h)
#     # try:4
#     width = int(w / 3)
#     im2 = cv2.imread(im2)
#     f = open('test.txt', 'a')
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
#     cropped = im2[y:y + h, x:x + w]
#     img = cv2.resize(rect, (1020, 750))
#     cv2.imshow('d', img)
#     cv2.waitKey(0)
#     # count=count+1
#     text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
#     # print(text)
#     f = open('sample.txt', 'w')
#     f.write(text)
#     f.close()
#
#
# for i in os.listdir(folder_path):
#     file = i
#     main_convert(5, 5, 1240, 450, im2=f"{folder_path}\{i}")
#
#     f = open('sample.txt', 'r')
#     x = f.readlines()
#     dic = {}
#     voterID = x[0]
#     lastname = x[3]
#     husband_lastname = x[6]
#
#     for i in x:
#         dic['Voter_file_tracker'] = file
#         dic['Voter_id'] = voterID
#
#         if "Name " in i:
#             Name = i.split("Name")[1]+lastname
#             dic["Name"] = Name
#             print(Name)
#             # rec = mycollection.insert_one(dic)
#         if i.startswith("Husband's Name"):
#             father_name = i.replace("Husband's Name", '') + husband_lastname
#             dic["Husband's Name"] = father_name
#             print(father_name)
#         # if i.startswith("Husband's Name"):
#         #     father_name = i.replace("Husband's Name", '') + husband_lastname
#         #     dic["Husband's Name"] = father_name
#         #     print(father_name)
#         elif i.startswith("House Number"):
#             House_Number = i.replace("House Number", '')
#             dic['House Number'] = House_Number
#             print(House_Number)
#
#         elif i.startswith("Age"):
#             age = str(i)[5:7]
#             print(age)
#             gender = str(i)[16:22]
#             print(gender)
#
#             dic["Age"] = age
#             dic["Gender"] = gender
#
#     rec = mycollection.insert_one(dic)






######################################this code use Name and fathers and Age names double line ##########################
#
# import pytesseract
#
# import cv2
# import os
# from pymongo import MongoClient
#
#
# folder_path = r'C:\Users\vivif\Desktop\Name double lines'
#
# # creation of MongoClient
# client = MongoClient()
# # he = []
#
#
# # Connect with the portnumber and host
# client = MongoClient('mongodb://localhost:27017/')
# # client = MongoClient('mongodb://%s:%s@13.234.70.44:27017' % (username,password))
#
# # Access database
# mydatabase = client['voterImage']
#
# # Access collection of the database
# mycollection = mydatabase['Single_voter_image']
#
# # myimage = mydatabase['test2']
#
# # dictionary to be added in the database
#
#
# # poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
#
# def main_convert(x, y, w, h, im2, img_file=None):
#     # print(h)
#     # try:4
#     width = int(w / 3)
#     im2 = cv2.imread(im2)
#     f = open('test.txt', 'a')
#     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
#     cropped = im2[y:y + h, x:x + w]
#     img = cv2.resize(rect, (1020, 750))
#     cv2.imshow('d', img)
#     cv2.waitKey(1)
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
#     # print(file)
#     main_convert(5, 5, 1240, 450, im2=f"{folder_path}\{i}")
#
#     f = open('sample.txt', 'r')
#     x = f.readlines()
#     dic = {}
#     voterID = x[0]
#
#     for i in x:
#         dic['Voter_file_tracker'] = file
#         dic['Voter_id'] = voterID
#         lastname = x[3]
#         fathers_name = x[6]
#         house_number = x[8]
#         # print(voterID)
#         # print(i[0:10])
#         if i.startswith('Name'):
#             # if "Name" in i:
#             Name = i.replace('Name', '').replace(':', '').replace(' ', '').replace('-', '').strip()+lastname
#             dic['Name'] = Name
#             print('Name',Name)
#
#         if i.startswith("Father's Name"):
#
#             father_name = i.replace("Father's Name", '').replace(':', '').replace(' ', '').replace('-',
#                                                                                                             '').strip()+fathers_name
#             dic["Father's Name"] = father_name
#             print(father_name)
#
#
#         elif i.startswith("Husband's Name"):
#             husband_name = i.replace("Husband's Name", '').replace(':', '').replace(' ', '').replace('-','').strip()+fathers_name
#             dic["Husband's Name"] = husband_name
#             print(husband_name)
#
#
#         elif i.startswith("Mother's Name"):
#             Mother_Name = i.replace("Mother's Name", '').replace(':', '').replace(' ', '').replace('-',
#                                                                                                             '').strip()+fathers_name
#             dic["Mother's Name"] = Mother_Name
#             print(Mother_Name)
#
#
#         elif i.startswith("House Number"):
#             House_Number = i.replace("House Number", '').replace(':', '').replace(' ', '').replace(';',
#                                                                                                           '').strip()+house_number
#             dic['House Number'] = House_Number
#             print(House_Number)
#
#         elif i.startswith("Age"):
#             age = str(i)[5:7]
#             print(age)
#             gender = str(i)[16:22]
#             print(gender)
#
#             dic["Age"] = age
#             dic["Gender"] = gender
#             print(voterID)
#             rec = mycollection.insert_one(dic)

























# import pytesseract
# import cv2
# import os
# from pymongo import MongoClient
#
# # Path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# folder_path = r'C:\Users\vivif\Desktop\Name double lines'
#
# # Create a MongoClient
# client = MongoClient('mongodb://localhost:27017')
#
# # Access database
# mydatabase = client['voterImage']
#
# # Access collection of the database
# mycollection = mydatabase['Single_voter_image']
#
# def extract_info_from_image(image_path):
#     im2 = cv2.imread(image_path)
#     text = pytesseract.image_to_string(im2, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789')
#     return text.splitlines()
#
# def main():
#     for image_filename in os.listdir(folder_path):
#         image_path = os.path.join(folder_path, image_filename)
#         extracted_info = extract_info_from_image(image_path)
#
#         data = {}
#         data['Voter_file_tracker'] = image_filename
#
#         for line in extracted_info:
#             if "Name" in line:
#                 data['Name'] = line.split("Name")[1].strip()
#
#             if "Husband's Name" in line:
#                 data['Husband\'s Name'] = line.split("Husband's Name")[1].strip()
#
#             if "Father's Name" in line:
#                 data['Father\'s Name'] = line.split("Father's Name")[1].strip()
#
#             if "House Number" in line:
#                 data['House Number'] = line.split("House Number")[1].strip()
#
#             if "Age" in line:
#                 data['Age'] = line.split("Age")[1].strip()
#
#             if "Gender" in line:
#                 data['Gender'] = line.split("Gender")[1].strip()
#
#         # Insert the data into MongoDB
#         mycollection.insert_one(data)
#
# if __name__ == "__main__":
#     main()
