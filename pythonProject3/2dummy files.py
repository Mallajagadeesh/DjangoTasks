# image =r'C:\Users\vivif\pythonProject\pythonProject3\SAMPLE\page1.pdf0.png'
# image =r'C:\Users\vivif\Desktop\images 2'
# for i in image:
#     print(i)
import os
folder_path = r'C:\Users\vivif\Desktop\images 2'
x = os.listdir(folder_path)
for i in x:
    print(i)
