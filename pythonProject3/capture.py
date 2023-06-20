import cv2
import pytesseract
import pymongo
from pymongo import MongoClient

poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
output = r'C:\Users\vivif\pythonProject\pythonProject3'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
mydatabase = client['Data_conversion2']

# Access collection of the database
mycollection = mydatabase['Anakapalli']
mycollection2 = mydatabase['Anakapalli']
myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}
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

            rec = mycollection.insert_one({
                })


def ima(x, y, w, h, im2, img_file):
    # #print(x,y)
    im2 = cv2.imread(im2)
    cv2.putText(im2, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    covert(x, y, w, h, im2, img_file)
area = []
value = []

def img_detect(img_path, img_file=None):
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
        xa = value[i][2]
        ya = value[i][3]
        l = value[i][0]
        w = value[i][1]

        ima(x=xa, y=ya, w=w, h=l, im2=img_path, img_file=img_file)






# converting_pdftoimg(r"C:\Users\vivif\Desktop\firstpage.pdf")
# img_detect(img_path=r'C:\Users\vivif\Desktop\firstpage_page-0001.jpg')
text = pytesseract.image_to_string(r"C:\Users\vivif\pythonProject\pythonProject3\SAMPLE\First image.jpg",config='--psm 6 --oem 1')
print(text)