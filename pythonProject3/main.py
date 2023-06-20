# # # sets = {"a","b","c","tdgfds","jhgtifk","a","b","c"}
# # # print(sets)
# # #
# # #
# # # list = ["a","b","c","tdgfds","jhgtifk","a","b","c"]
# # # print(list)
# # #
# # #
# # # tuple = ("a","b","c","tdgfds","jhgtifk","a","b","c")
# # # print(tuple)
# #
# # # a = ["dots", "jagan", "cr", "hr", "madhu", "hs"]
# # # for x in a:
# # #     if x == "jagan" or x == "hr" or x == "madhu":
# # #         print(x)
# # #     else:
# # #         print("fail")
# #
# #
# # a = 35
# # b = 45
# # c = 60
# # if a > b and c > b:
# #     print("both are not same")
# #
# #
# #
# # a = "slip100223_AP_Anakapalli_Madugula_207_jogannapalem_M.P.P SCHOOL.,KINTHADA SIVARU JOGANNAPALEM.pdf19.png.png"
# # # for x in a:
# # #     print(x)
# # #     for i in a:
# # #         print(i)
# # x = a.split()
# # print(x)
# # # print(a[:1])
# #
# #
# # b = ['slip100223_AP_Anakapalli_Madugula_207_jogannapalem_M.P.P', 'SCHOOL.,KINTHADA', 'SIVARU', 'JOGANNAPALEM.pdf19.png.png']
# # for x in b:
# #     print(x)
# #
# # x = b.count("SCHOOL.,KINTHADA")
#
# # import PyPDF2
# # import os
# # a = r"C:\Users\vivif\Desktop\convert2\pdfs"
# # l = os.listdir(a)
# # for x in l:
# #     print(x)
# #
# # print(len(l))
# # file = open(r'C:\Users\vivif\Desktop\convert2\pdfs\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf', 'rb')
# # y = PyPDF2.PdfFileReader(file)
# # print(y.numPages)
#
# # C:\Users\vivif\Desktop\convert2\pdfs\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf
#
# #
# # # importing required modules
# # import PyPDF2
# # # we can install pip install 'PyPDF2<3.0'
# # # creating a pdf file object
# #
# #
# # pdfFileObj = open(r'C:\Users\vivif\Desktop\convert2\pdfs\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf', 'rb')
# #
# # # creating a pdf reader object
# # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# #
# # # printing number of pages in pdf file
# # print(pdfReader.numPages)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
# # # this code all pdfs count and images count
# # import PyPDF2
# # import os
# # a = r"C:\Users\vivif\Desktop\convert2\pdfs"   # file path  ALL PDFS PATH
# # l = os.listdir(a)
# # for x in l:
# #     file_path = os.path.join(a,x)
# #     file = open(file_path, 'rb')
# #     y = PyPDF2.PdfFileReader(file)
# #     print(file)
# #     print(y.numPages)
# # # |
# # # |
# # # this pdfs count code
# # # a = r"C:\Users\vivif\Desktop\convert2\pdfs"
# # # l = os.listdir(a)
# # # print(len(l))
#
# # text = "tyfgfgt hygy huh"
# # x = text.split(' ')
# # print(x)
#
# # tex = "AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf2.png"
# # x = tex.split("_")
# # # x1 = tex.split(',')
# # # h = []
# # # x.tex.split(',')
# # print(x)
# # # for x in x:
# # #     h.append(x)
# # #     print(x)
# # # print(h)
# # # print(len(x))
# import re
# tex = "AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf2.png"
# x = re.split("_|,",tex)
# print(x)
# # word = ""
# # for a in tex:
# #     if a == "_" or a == ",":
# #         word= word + ""
# #     else:
# #         word= word + a
# # print(word)
# # g = word.split()
# # for x in g:
# #     print(x)
# # print(x)
#
#
# # from autorun2 import output_file
#
# txt = "Hello, welcome, to my, world."
# x = txt.split( )
# print(x)
# x = txt.count("welcome to my world.")
# print(x)


# import PyPDF2 as pdf
#
# poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
#
#
# def converting_pdftoimg(pdf_path):
#     x = pdf.PdfReader(pdf_path)
#     page_length = (x.numPages)
#     from pdf2image import convert_from_path
#     images = convert_from_path(pdf_path, 500, poppler_path=poppler_path)
#     name = pdf_path.split("\\")
#     for i, image in enumerate(images):
#         if i>0:
#             if i==(page_length-1):
#                 pass
#             elif i==2:
#                 pass
#             else:
#                 print(i, 'is pdf converting into images')
#                 fname = f'{name[-1]}' + str(i) + '.png'
#                 image.save(fr"C:\Users\vivif\pythonProject\pythonProject3\pdfs\{fname}", "PNG")
#         elif i==0:
#             print(i, 'is pdf converting into images')
#             fname = f'main_{name[-1]}' + str(i) + '.png'
#             image.save(fr"C:\Users\vivif\pythonProject\pythonProject3\pdfs\{fname}", "PNG")
#
#
# pdf_path=r"C:\IVIN Electoral Data\jagadeesh Download\Anakapalli\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf"
# converting_pdftoimg(pdf_path=pdf_path)


# Driver Program
string = '_ g e e k vfvfd fd f '
print(string.replace(" _ ", ""))
x = string.replace(" ", "",).replace("_","")
print(x)
# a = "jag"
# a = "bh"
