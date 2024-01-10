import os
from pdf2image import convert_from_path

folder_path = r'C:\Users\vivif\Documents\2024_data_pdf'  ## give pdf's folder path
output_file = r'C:\Users\vivif\Documents\2024_image'


def converting_pdftoimg(pdf_path):
    # Specify the path to the Poppler executable
    poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'

    # Convert PDF to images
    images = convert_from_path(pdf_path, 500, poppler_path=poppler_path)

    # Extract the name of the PDF file
    name = pdf_path.split("\\")
    print(name)

    # Save each image with a unique name
    for i, image in enumerate(images):
        fname = f'{name[-1]}' + str(i) + '.png'
        image.save(f"{output_file}\{fname}", "PNG")
        print(fname)


# Example usage:
l = os.listdir(folder_path)
for i in range(len(l)):
    converting_pdftoimg(pdf_path=f'{folder_path}\{l[i]}')
