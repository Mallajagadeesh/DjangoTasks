# poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# output_file = r'C:\Users\vivif\Desktop\dummy original images 2'
# folder_path = r'C:\Users\vivif\Desktop\dummy pdfs'


import cv2
import numpy as np
import pytesseract
import os
import PyPDF2 as pdf

import datetime
import base64



# C:\Program Files\Tesseract-OCR\tesseract.exe
# poppler_path=r'D:\downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'
poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Mongodb
from pymongo import MongoClient

# output_file = r'D:\projects\pytesseract\images'  ## give images folder path
output_file = r'C:\Users\vivif\Desktop\image1'
folder_path = r'C:\Users\vivif\Desktop\dummy pdfs'  ## give pdf's folder path
# creation of MongoClient
client = MongoClient()
he = []
import urllib.parse

Username = 'devops_admin'
Password = 'Devops1234'
username = urllib.parse.quote_plus(Username)
password = urllib.parse.quote_plus(Password)
client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('mongodb://%s:%s@13.234.70.44:27017' % (username,password))

# Access database
mydatabase = client['Data_conversion5']

# Access collection of the database
mycollection = mydatabase['Anakapalli3']
mycollection2 = mydatabase['Anakapalli3']
myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

# Time kosam

dt = datetime.datetime.now()
print(dt)
lis = ["", ""]
main_page_data = []

count = 0


def imgetobase(file, img_file):
    global count
    f = f"slip{count}-{img_file}.png"
    import boto3
    b_name = "ivin-pro-data-conversion"
    # s3 = boto3.client("s3")
    # b_res = s3.list_buckets()
    # for i in b_res['Buckets']:
    #         print(i)

    cv2.imshow('Resized', file)
    img = cv2.imwrite(f, file)
    cv2.waitKey(3)
    count = 1 + count
    # with open(f, 'rb') as img:
    #     s3.upload_fileobj(img, b_name, img_file + f)
    return f


# def pagetobase(image):
#     image = open(image, 'rb')
#     image_read = image.read()
#     image_64_encode = base64.encodebytes(image_read) #encodestring also works aswell as decodestring
#     # print('This is the image in base64: ' + str(image_64_encode))
#     return str(image_64_encode)


def page(image):
    text = pytesseract.pytesseract.image_to_string(image)
    # print(text)
    text.replace('Photo', "")
    # print(text)
    f = open('text.txt', 'w')
    f.write(text + "\n")
    f.close()
    fi = open('text.txt', 'r')
    x = fi.readlines()
    for i in x:
        if "Assembly" in i:
            lis[0] = i
        elif "Section" in i:
            lis[1] = i
    fi.close()


# print(lis)


c = 1


#

def covert(x, y, w, h, im2, img_file):
    # print(h)
    # try:
    width = int(w / 3)
    if h >= 400 and h < 1000:
        # print(h,w)
        width = int(w / 3)
        # print(width,'--------')
        f = open('test.txt', 'a')
        rect = cv2.rectangle(im2, (x, y), (x + width, y + h), (0, 255, 0), 5)

        if x == 0 and y == 0:
            pass
        else:
            cropped = im2[y:y + h, x:x + width]
            img = cv2.resize(rect, (1020, 750))
            cv2.imshow('d', cropped)
            cv2.waitKey(3)
            # count=count+1
            text = pytesseract.image_to_string(cropped)
            f = open('text.txt', 'a')
            f.write(text)
            f.close()
            b = imgetobase(cropped, img_file)
            rec = mycollection.insert_one({
                'Voter_file_tracker': img_file,
                "Mandal":main_page_data[0],
                "votere_slip": b,
                "Assembly Name": lis[0],
                "Section": lis[1],
                'details': text,
                'Created on': dt})


def ima(x, y, w, h, im2, img_file):
    # #print(x,y)
    im2 = cv2.imread(im2)
    cv2.putText(im2, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    # rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    # img = cv2.resize(rect, (1020, 750))
    # cv2.imshow('d', img)
    # print(x, y)
    covert(x, y, w, h, im2, img_file)
    W = int(w / 3)
    covert(x + W, y, w, h, im2, img_file)
    covert(x + W + W, y, w, h, im2, img_file)


area = []
value = []


# def img_detect(img_path, img_file):
#     lis.clear()
# page(img_path)
#
def img_detect(img_path, img_file):
    page(img_path)
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
        x1, y1 = cnt[0][0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)

            ratio = float(w) / h
            if ratio >= 0.9 and ratio <= 1.1:
                pass
            else:
                area.append((h * w))
                value.append((h, w, x, y))
                he.append(h)
    for i in range(len(area)):
        # if value[i][1]>=0 and value[i][1]>100:
        xa = value[i][2]
        ya = value[i][3]
        l = value[i][0]
        w = value[i][1]
        # cv2.rectangle(img, (xa, ya), (xa + w, ya + l), (0, 255, 0), 2)
        ima(x=xa, y=ya, w=w, h=l, im2=img_path, img_file=img_file)


import os


def image_upload(image_file):
    print("count of images :", len(os.listdir(folder_path)))
    l = os.listdir(image_file)
    path = image_file
    print(l)
    for k in range(len(l)):
        # print('sir done')
        print(k, 'started')
        area.clear()
        value.clear()
        he.clear()
        print(l[k])
        if l[0]:
            main_convert(1800, 1600, 300, 300, im2=l[k])
        else:
            img_detect(img_path=f"{path}\{l[k]}", img_file=l[k])
            os.remove(f"{path}\{l[k]}")
            print(k, 'done')


def converting_pdftoimg(pdf_path):
    from pdf2image import convert_from_path
    x = pdf.PdfReader(pdf_path)
    page_length = (x.numPages)
    # print(pdf_path)
    images = convert_from_path(pdf_path, 500, poppler_path=poppler_path)
    name = pdf_path.split("\\")
    print(name)
    for i, image in enumerate(images):
        if i > 0:
            if i == (page_length - 1):
                pass
            elif i == 2:
                pass
            else:
                print(i, 'is pdf converting into images')
                fname = f'{name[-1]}' + str(i) + '.png'
                image.save(f"{folder_path}\{fname}", "PNG")
        elif i == 0:
            print(i, 'is pdf converting into images')
            fname = f'{name[-1]}' + str(i) +'.png'
            image.save(f"{folder_path}\{fname}", "PNG")



def main_convert(x, y, w, h, im2,):
    print(h)
    main_page_data.clear()
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
    f = open('main_page.txt', 'a')
    f.write(text)
    f.close()

    f = open('main_page.txt', 'r')
    x = f.readlines()
    # print(x)
    for i in x:
        if "Mandal" in i:
            main_page_data.append(i)
        elif 'Main Town/Village' in i:
            main_page_data.append(i)
        elif 'Police Station' in i:
            main_page_data.append(i)
        elif 'Revenue Division' in i:
            main_page_data.append(i)
        elif 'District' in i:
            print(i)
            main_page_data.append(i)


l = os.listdir(folder_path)
# print(l)
#
for i in range(len(l)):


    converting_pdftoimg(pdf_path=f'{folder_path}\{l[i]}')

image_upload(f'{folder_path}')

# dt  = datetime.datetime.now()
