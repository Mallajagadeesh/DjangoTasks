# this code all pdfs count and images count
import PyPDF2
import os
a = r"C:\Users\vivif\Desktop\convert2\pdfs"   # file path  ALL PDFS PATH
l = os.listdir(a)
for x in l:
    file_path = os.path.join(a,x)
    file = open(file_path, 'rb')
    y = PyPDF2.PdfFileReader(file)
    print(file)
    print(y.numPages)
# |
# |
# this pdfs count code
# a = r"C:\Users\vivif\Desktop\convert2\pdfs"
# l = os.listdir(a)
# print(len(l))