# # import PyPDF2
# #
# # def extract_first_page(pdf_path):
# #     # Open the PDF file in read-binary mode
# #     with open(pdf_path, "rb") as file:
# #         # Create a PDF reader object
# #         reader = PyPDF2.PdfReader(file)
# #
# #         # Get the first page of the PDF
# #         first_page = reader.pages[0]
# #
# #         # Extract the text content from the first page
# #         text = first_page.extract_text()
# #
# #         # Print or process the extracted text
# #         print(text)
# #
# # # Provide the path to your PDF file
# # pdf_path = r'C:\IVIN Electoral Data\jagadeesh Download\Anakapalli\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf'
# #
# # # Call the function to extract the first page
# # extract_first_page(pdf_path)


# second
#
# import PyPDF2
# import os
# def extract_first_page(folder_path):
#     with open(folder_path, 'rb') as file:
#         reader = PyPDF2.PdfFileReader(file)
#         first_page = reader.getPage(0)
#         output = PyPDF2.PdfFileWriter()
#         output.addPage(first_page)
#
#         # Save the first page as a new PDF file
#         with open('firstsec_page.pdf', 'wb') as output_file:
#             output.write(output_file)
#
# # Provide the path to your PDF file
# folder_path = r'C:\IVIN Electoral Data\jagadeesh Download\Anakapalli\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf'
#
#
# output_file = r'C:\Users\vivif\Desktop\image1'
# # Call the function to extract the first page
# extract_first_page(folder_path)

# import PyPDF2
#
# def extract_first_page(pdf_path, output_path):
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfFileReader(file)
#         first_page = reader.getPage(0)
#
#         writer = PyPDF2.PdfFileWriter()
#         writer.addPage(first_page)
#
#         with open(output_path, 'wb') as output_file:
#             writer.write(output_file)
#
# # Example usage
# pdf_path = r'C:\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf'
# output_path = r'C:\Users\vivif\Desktop\image1'
#
# extract_first_page(pdf_path, output_path)
















# import PyPDF2
#
# input_file = r"C:\IVIN Electoral Data\jagadeesh Download\Anakapalli\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf"
#
# page = 0
#
# # Creating a pdf file object
# pdfFileObj = open(r'C:\IVIN Electoral Data\jagadeesh Download\Anakapalli\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf', 'rb')
#
# # Creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # Creating a page object
# pageObj = pdfReader.getPage(page)
#
# # Extracting text from page
# data = pageObj.extractText()
#
# # Closing the pdf file object
# pdfFileObj.close()
#
# print(data)




#
# x = "fdskjgsfong"
# for i in x:
#     print(i[0])
# print(x[0])
# letter =[]
# # for i in range(1):
# #     print(x)
# # g = x.split()
# # print(g)
# for g in x:
#     letter.append(x[0])
#     print(g)
# for i in x:
#     if x == f:
#         print("success")






# a = "C:\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf"
# f = open("C:\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf","rb")
# print(f)
import os
# folder_path = r'C:\Anakapalli\AP_Anakapalli_Anakapalle_1_Teeda_M.P.Ele.School,Eastern Side,Teeda TEEDA.pdf'
# l = os.listdir(folder_path)
# print(folder_path)
# for i in range(len(l)):
#    print(l[i])
   # converting_pdftoimg(pdf_path=f'{folder_path}\{l[i]}')

# import module
import pdf2image
from pdf2image import convеrt_from_path

# pages = convert_from_path('example.pdf')
#
# for i in range(len(pages)):
#     print(i)
#
# # pages[i].save('page'+ str(i) +'.jpg', 'JPEG')

import pdf2image

folder_path = r"C:\Anakapalli"
l = os.listdir(folder_path)
print(l)
for i in range(len(l)):
    print(l[i])
    convеrt_from_path(pdf_path=f'{folder_path}\{l[i]}')
