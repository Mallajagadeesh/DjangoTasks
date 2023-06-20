# import pytesseract
# import cv2
#
#
#
# def covert(x, y, w, h, im2, img_file):
#     # print(h)
#     # try:
#     width = int(w / 3)
#     if h >= 400 and h < 1000:
#         # print(h,w)
#         width = int(w / 3)
#         # print(width,'--------')
#         f = open('test.txt', 'a')
#         rect = cv2.rectangle(im2, (x, y), (x + width, y + h), (0, 255, 0), 5)
#
#         if x == 0 and y == 0:
#             pass
#         else:
#             cropped = im2[y:y + h, x:x + width]
#             img = cv2.resize(rect, (1020, 750))
#             cv2.imshow('d', cropped)
#             cv2.waitKey(3)
#             # count=count+1
#             text = pytesseract.image_to_string(cropped)
#             f = open('text.txt', 'a')
#             f.write(text)
#             f.close()
#             b = imgetobase(cropped, img_file)
#
#
# text = pytesseract.image_to_string(r"C:\Users\vivif\pythonProject\pythonProject3\SAMPLE\First image.jpg",config='--psm 6 --oem 1')
# print(text)
#
# a = ["dnewbd", "2", "1", "mckd", "jagan", "madhu"];
# for x in a:
#     a = []
#     if x == "1":
#
#
#     else:
#         print("no data")


# a = 5
# b = 9
# for x in range(6):
#     print(x)
import  pytesseract

import cv2
poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
output = r'C:\Users\vivif\pythonProject\pythonProject3'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



def covert(x, y, w, h, im2, img_file=None):
    print(h)
    # try:
    width = int(w / 3)
    im2 = cv2.imread(im2)
    f = open('test.txt', 'a')
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cropped = im2[y:y + h, x:x + w]
    img = cv2.resize(rect, (1020, 750))
    cv2.imshow('d', img)
    cv2.waitKey(0)
    # count=count+1
    text = pytesseract.image_to_string(cropped,config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')

    # print(text)
    f = open('sample.txt', 'a')
    f.write(text)
    f.close()



# image =r'C:\Users\vivif\pythonProject\pythonProject3\SAMPLE\page1.pdf0.png'
image =r'C:\Users\vivif\Desktop\images 2'
for i in range(len(image)):
   print(image[i])
   # converting_pdftoimg(pdf_path=f'{image}\{l[i]}')
covert(1800,1600,2000,1500,im2=image)
# covert(1800,1600,300,300,im2=r'C:\Users\vivif\pythonProject\pythonProject3\SAMPLE\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf')

f= open('sample.txt','r')
x = f.readlines()
# print(x)
for i in x:
    if "Mandal" in i:
        print(i)
    elif 'Main Town/Village' in i:
        print(i)
    elif 'Police Station' in i:
        print(i)
    elif 'Revenue Division' in i:
        print(i)
    elif 'District' in i:
        print(i)