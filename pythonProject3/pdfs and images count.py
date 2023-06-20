# this code all pdfs count and images count
import PyPDF2
import os
a = r"C:\IVIN Electoral Data\Rajesh Download 27-03-2023\1_Srikakulam\1_AP_Srikakulam_Palasa"   # file path  ALL PDFS PATH
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


