################### When the run this code slips are converted ############
#
# import cv2
# import numpy as np
#
# img = cv2.imread(r"C:\Users\vivif\Documents\2024_image\Frame 11.pdf0.png")
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# ret, thresh = cv2.threshold(gray, 50, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, 1, 2)
# print("Number of contours detected:", len(contours))
# c = 0
# for cnt in contours:
#     x1, y1 = cnt[0][0]
#     approx = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)
#     if len(approx) == 4:
#         x, y, w, h = cv2.boundingRect(cnt)
#         ratio = float(w) / h
#         area = h + w
#         if ratio >= 0.9 and ratio <= 1.1 or area < 1000:
#             pass
#         #  img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
#         #  cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
#         else:
#             #  cv2.putText(img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#             print(h + w, x, y)
#             # img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#             cropped = img[y:y + h, x:x + w]
#             x = cv2.resize(img, (720, 480))
#             c = c + 1
#             cv2.imwrite(f'cropped{c}.png', cropped)
#             cv2.imshow("Shapes", cropped)
#             cv2.waitKey(3)
#
#


######################   This code use of slips filename saved  ######################
# import cv2
# import os
#
# img_path = r"C:\Users\vivif\Documents\2024_image\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf2_11.png"
#
# # Extract filename without extension
# filename = os.path.splitext(os.path.basename(img_path))[0]
#
# img = cv2.imread(img_path)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# ret, thresh = cv2.threshold(gray, 50, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, 1, 2)
# print("Number of contours detected:", len(contours))
# c = 0
#
# for cnt in contours:
#     x1, y1 = cnt[0][0]
#     approx = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)
#     if len(approx) == 4:
#         x, y, w, h = cv2.boundingRect(cnt)
#         ratio = float(w) / h
#         area = h + w
#         if ratio >= 0.9 and ratio <= 1.1 or area < 1000:
#             pass
#         else:
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#             cropped = img[y:y + h, x:x + w]
#             x = cv2.resize(img, (720, 480))
#             c = c + 1
#             save_path = f'{filename}{c}.png'
#             cv2.imwrite(save_path, cropped)
#             cv2.imshow("Shapes", cropped)
#             cv2.waitKey(3)


###############################  This code use slips image converted and also filename also given perfect   ##########################
#
# import cv2
# import os
#
# # Original image file path
# img_path = r'C:\Users\vivif\Documents\2024_image\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf2.png'
#
# # Load the image
# img = cv2.imread(img_path)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# ret, thresh = cv2.threshold(gray, 50, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, 1, 2)
# print("Number of contours detected:", len(contours))
# c = 0
#
# # Get the original file name without extension
# original_filename = os.path.splitext(os.path.basename(img_path))[0]
#
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     approx = cv2.approxPolyDP(cnt, 0.09 * cv2.arcLength(cnt, True), True)
#     if len(approx) == 4:
#         ratio = float(w) / h
#         area = h + w
#         if ratio >= 0.9 and ratio <= 1.1 or area < 1000:
#             pass
#         else:
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#             cropped = img[y:y + h, x:x + w]
#             x = cv2.resize(img, (420, 480))
#             c = c + 1
#             # Append the contour index to the original file name
#             new_filename = f'{original_filename}{c}.png'
#             cv2.imwrite(new_filename, cropped)
#             cv2.imshow("Shapes", cropped)
#             cv2.waitKey(3)
#
# cv2.destroyAllWindows()
#

# import cv2
# import pytesseract
#
# # Load the image
# image = cv2.imread(r'C:\Users\vivif\Documents\2024_image\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf2.png')
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply any necessary preprocessing steps (e.g., resizing, thresholding, etc.)
#
# # Use Tesseract OCR to extract text from the image
# text = pytesseract.image_to_string(gray_image)
#
# # Print the extracted text
# print(text)



####################Finally code is working but some small also saved ##########################
#
# import cv2
# import pytesseract
# import numpy as np
#
# # Load the image
# image_path = r'C:\Users\vivif\Documents\2024_image\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf3.png'
# image = cv2.imread(image_path)
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply any necessary preprocessing steps (e.g., resizing, thresholding, etc.)
#
# # Use a simple threshold to binarize the image
# _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
#
# # Find contours around the boxes
# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize lists to store the coordinates of each box
# box_coordinates = []
#
# # Iterate through each contour
# for contour in contours:
#     # Get the coordinates of the bounding box around the contour
#     x, y, w, h = cv2.boundingRect(contour)
#
#     # Ensure the box is not too small (adjust the threshold as needed)
#     if w > 10 and h > 10:
#         box_coordinates.append((x, y, w, h))
#
# # Sort the box coordinates by y-coordinate and then by x-coordinate
# box_coordinates.sort(key=lambda box: (box[1], box[0]))
#
# # Define the number of rows and columns
# num_rows = 4
# num_columns = 10
#
# # Iterate through the box coordinates and crop/save each box
# for i, (x, y, w, h) in enumerate(box_coordinates):
#     # Calculate the row and column index
#     row_index = i // num_columns
#     col_index = i % num_columns
#
#     # Crop the box from the original image
#     box = image[y:y + h, x:x + w]
#
#     # Save the cropped box
#     box_path = f'box_{row_index}_{col_index}.png'
#     cv2.imwrite(box_path, box)
#
#     print(f'Box {i + 1} saved as {box_path}')
#
#
#




#
# import cv2
# import numpy as np
#
# # Load the image
# image_path = r'C:\Users\vivif\Documents\2024_image\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf3.png'
# image = cv2.imread(image_path)
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply any necessary preprocessing steps (e.g., resizing, thresholding, etc.)
#
# # Use adaptive thresholding to binarize the image
# binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#
# # Find contours around the boxes
# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize lists to store the coordinates of each box
# box_coordinates = []
#
# # Iterate through each contour
# for contour in contours:
#     # Get the coordinates of the bounding box around the contour
#     x, y, w, h = cv2.boundingRect(contour)
#
#     # Ensure the box is not too small (adjust the threshold as needed)
#     if w > 10 and h > 10:
#         box_coordinates.append((x, y, w, h))
#
# # Sort the box coordinates by y-coordinate and then by x-coordinate
# box_coordinates.sort(key=lambda box: (box[1], box[0]))
#
# # Visualize the detected boxes on the original image
# for (x, y, w, h) in box_coordinates:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
#
# cv2.imshow('Detected Boxes', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Define the number of rows and columns
# num_rows = 3
# num_columns = 10
#
# # Iterate through the box coordinates and crop/save each box
# for i, (x, y, w, h) in enumerate(box_coordinates):
#     # Calculate the row and column index
#     row_index = i // num_columns
#     col_index = i % num_columns
#
#     # Crop the box from the original image
#     box = image[y:y + h, x:x + w]
#
#     # Save the cropped box
#     box_path = f'box_{row_index}_{col_index}.png'
#     cv2.imwrite(box_path, box)
#
#     print(f'Box {i + 1} saved as {box_path}')






##################### This code are size images Download ####################
# import cv2
# import os
#
# # Load the image
# image_path = r'C:\Users\vivif\Documents\2024_image\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf3.png'
# image = cv2.imread(image_path)
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply any necessary preprocessing steps (e.g., resizing, thresholding, etc.)
#
# # Use adaptive thresholding to binarize the image
# binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#
# # Find contours around the boxes
# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize lists to store the coordinates of each box
# small_boxes = []
# large_boxes = []
#
# # Iterate through each contour
# for contour in contours:
#     # Get the coordinates of the bounding box around the contour
#     x, y, w, h = cv2.boundingRect(contour)
#
#     # Ensure the box is not too small (adjust the threshold as needed)
#     if w > 10 and h > 10:
#         if w < 1200 and h < 600:
#             small_boxes.append((x, y, w, h))
#         else:
#             large_boxes.append((x, y, w, h))
#
# # Sort the box coordinates by y-coordinate and then by x-coordinate
# small_boxes.sort(key=lambda box: (box[1], box[0]))
# large_boxes.sort(key=lambda box: (box[1], box[0]))
#
# # Visualize the detected boxes on the original image
# for (x, y, w, h) in small_boxes + large_boxes:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
#
# cv2.imshow('Detected Boxes', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Create folders if they don't exist
# small_boxes_folder = 'small_boxes'
# large_boxes_folder = 'large_boxes'
#
# os.makedirs(small_boxes_folder, exist_ok=True)
# os.makedirs(large_boxes_folder, exist_ok=True)
#
# # Iterate through the small boxes and save each box
# for i, (x, y, w, h) in enumerate(small_boxes):
#     box_path = os.path.join(small_boxes_folder, f'box_{i}.png')
#     box = image[y:y + h, x:x + w]
#     cv2.imwrite(box_path, box)
#     print(f'Small box {i + 1} saved as {box_path}')
#
# # Iterate through the large boxes and save each box
# for i, (x, y, w, h) in enumerate(large_boxes):
#     box_path = os.path.join(large_boxes_folder, f'box_{i}.png')
#     box = image[y:y + h, x:x + w]
#     cv2.imwrite(box_path, box)
#     print(f'Large box {i + 1} saved as {box_path}')





################################### This code are filename with saved   ###########################
# import cv2
# import os
#
# # Load the image
# image_path = r'C:\Users\vivif\Documents\2024_image\2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-1-WI.pdf3.png'
# image = cv2.imread(image_path)
#
# # Extract the original image filename without extension
# file_name = os.path.splitext(os.path.basename(image_path))[0]
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply any necessary preprocessing steps (e.g., resizing, thresholding, etc.)
#
# # Use adaptive thresholding to binarize the image
# binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#
# # Find contours around the boxes
# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize lists to store the coordinates of each box
# small_boxes = []
# large_boxes = []
#
# # Iterate through each contour
# for contour in contours:
#     # Get the coordinates of the bounding box around the contour
#     x, y, w, h = cv2.boundingRect(contour)
#
#     # Ensure the box is not too small (adjust the threshold as needed)
#     if w > 10 and h > 10:
#         if w < 1200 and h < 600:
#             small_boxes.append((x, y, w, h))
#         else:
#             large_boxes.append((x, y, w, h))
#
# # Sort the box coordinates by y-coordinate and then by x-coordinate
# small_boxes.sort(key=lambda box: (box[1], box[0]))
# large_boxes.sort(key=lambda box: (box[1], box[0]))
#
# # Visualize the detected boxes on the original image
# for (x, y, w, h) in small_boxes + large_boxes:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
#
# cv2.imshow('Detected Boxes', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Create folders if they don't exist
# small_boxes_folder = 'small_boxes'
# large_boxes_folder = 'large_boxes'
#
# os.makedirs(small_boxes_folder, exist_ok=True)
# os.makedirs(large_boxes_folder, exist_ok=True)
#
# # Iterate through the small boxes and save each box
# for i, (x, y, w, h) in enumerate(small_boxes):
#     box_path = os.path.join(small_boxes_folder, f'{file_name}_small_box_{i}.png')
#     box = image[y:y + h, x:x + w]
#     cv2.imwrite(box_path, box)
#     print(f'Small box {i + 1} saved as {box_path}')
#
# # Iterate through the large boxes and save each box
# for i, (x, y, w, h) in enumerate(large_boxes):
#     box_path = os.path.join(large_boxes_folder, f'{file_name}_large_box_{i}.png')
#     box = image[y:y + h, x:x + w]
#     cv2.imwrite(box_path, box)
#     print(f'Large box {i + 1} saved as {box_path}')
#



################################# This code Multiple png at time will run ####################################
import cv2
import os

# Directory containing the images
images_directory = r'C:\Users\vivif\Documents\2024_image'

# Get a list of image files in the directory
image_files = [file for file in os.listdir(images_directory) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    # Load the image
    image_path = os.path.join(images_directory, image_file)
    image = cv2.imread(image_path)

    # Extract the original image filename without extension
    file_name = os.path.splitext(os.path.basename(image_path))[0]

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply any necessary preprocessing steps (e.g., resizing, thresholding, etc.)

    # Use adaptive thresholding to binarize the image
    binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours around the boxes
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize lists to store the coordinates of each box
    small_boxes = []
    large_boxes = []

    # Iterate through each contour
    for contour in contours:
        # Get the coordinates of the bounding box around the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Ensure the box is not too small (adjust the threshold as needed)
        if w > 10 and h > 10:
            if w < 1200 and h < 600:
                small_boxes.append((x, y, w, h))
            else:
                large_boxes.append((x, y, w, h))

    # Sort the box coordinates by y-coordinate and then by x-coordinate
    small_boxes.sort(key=lambda box: (box[1], box[0]))
    large_boxes.sort(key=lambda box: (box[1], box[0]))

    # Visualize the detected boxes on the original image
    for (x, y, w, h) in small_boxes + large_boxes:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)

    cv2.imshow('Detected Boxes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Create folders if they don't exist
    small_boxes_folder = 'small_boxes'
    large_boxes_folder = 'large_boxes'

    os.makedirs(small_boxes_folder, exist_ok=True)
    os.makedirs(large_boxes_folder, exist_ok=True)

    # Iterate through the small boxes and save each box
    for i, (x, y, w, h) in enumerate(small_boxes):
        box_path = os.path.join(small_boxes_folder, f'{file_name}_small_box_{i}.png')
        box = image[y:y + h, x:x + w]
        cv2.imwrite(box_path, box)
        print(f'Small box {i + 1} saved as {box_path}')

    # Iterate through the large boxes and save each box
    for i, (x, y, w, h) in enumerate(large_boxes):
        box_path = os.path.join(large_boxes_folder, f'{file_name}_large_box_{i}.png')
        box = image[y:y + h, x:x + w]
        cv2.imwrite(box_path, box)
        print(f'Large box {i + 1} saved as {box_path}')
