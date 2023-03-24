import PyPDF2
file = open('/home/madhu/Documents/django/sample.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(file)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(1)
print(pageObj.extractText())
file.close()