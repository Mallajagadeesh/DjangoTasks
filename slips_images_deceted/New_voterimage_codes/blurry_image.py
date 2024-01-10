# # # from PIL import Image
# # #
# # # def read_png(file_path):
# # #     try:
# # #         # Open the PNG file
# # #         image = Image.open(file_path)
# # #
# # #         # Display information about the image
# # #         print("Image Format:", image.format)
# # #         print("Image Mode:", image.mode)
# # #         print("Image Size:", image.size)
# # #
# # #         # You can also perform additional operations on the image if needed
# # #
# # #         # Close the image file
# # #         image.close()
# # #
# # #     except Exception as e:
# # #         print(f"Error: {e}")
# # #
# # # # Example usage
# # # png_file_path = r"C:\Users\vivif\PycharmProjects\Single_slip_images_Deceted\large_boxes\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf3_large_box_1.png"
# # # read_png(png_file_path)
# # #
# # #
# #
# #
# #
# #
# #
# # import cv2
# # import pytesseract
# #
# # # Install the required libraries:
# # # pip install pytesseract
# # # pip install opencv-python
# #
# # # Install Tesseract OCR from: https://github.com/tesseract-ocr/tesseract
# #
# # # Set the path to the Tesseract executable (update this path based on your installation)
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# #
# #
# # def perform_ocr(image_path):
# #     # Load the image
# #     image = cv2.imread(image_path)
# #
# #     # Convert the image to grayscale
# #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #
# #     # Apply thresholding or other preprocessing steps if needed
# #     # For example:
# #     # _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# #
# #     # Apply OCR using Tesseract
# #     custom_config = r'--oem 3 --psm 6'  # Adjust OCR engine mode and page segmentation mode as needed
# #
# #     text = pytesseract.image_to_string(gray, config=custom_config)
# #
# #     return text
# #
# #
# # if __name__ == "__main__":
# #     # Replace 'your_image.png' with the path to your image
# #     image_path = r'C:\Users\vivif\PycharmProjects\Single_slip_images_Deceted\large_boxes\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf10_large_box_2.png'
# #
# #     extracted_text = perform_ocr(image_path)
# #
# #     print("Extracted Text:")
# #     print(extracted_text)
# #
# #
#
#
#
import cv2
import pytesseract

# Install the required libraries:
# pip install pytesseract
# pip install opencv-python

# Install Tesseract OCR from: https://github.com/tesseract-ocr/tesseract

# Set the path to the Tesseract executable (update this path based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise (adjust the kernel size as needed)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding to enhance text features (adjust the parameters as needed)
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded


def perform_ocr(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)

    # Apply OCR using Tesseract
    custom_config = r'--oem 3 --psm 6'  # Adjust OCR engine mode and page segmentation mode as needed

    text = pytesseract.image_to_string(preprocessed_image, config=custom_config)

    return text


if __name__ == "__main__":
    # Replace 'your_image.png' with the path to your image
    image_path = r"C:\Users\vivif\PycharmProjects\Single_slip_images_Deceted\large_boxes\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf10_large_box_8.png"

    extracted_text = perform_ocr(image_path)

    # print("Extracted Text:")
    print(extracted_text)
