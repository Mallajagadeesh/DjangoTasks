from PIL import Image
import os
path = r"C:\Users\vivif\PycharmProjects\converstion file"
outputpath = r"C:\Users\vivif\PycharmProjects\anakapalli_slip voter images"
l = os.listdir(path)
for i in range(len(l)):
    print(l[i])
    png_image = Image.open(f'{path}\{l[i]}')
    png_image.save(f'{outputpath}\{l[i]}.webp', "webp")


# from PIL import Image
# import os
# path = r'images folder path'
# outputpath = r"storage folder path"
# l = os.listdir(path)
# for i in range(len(l)):
#     print(l[i])
#     png_image = Image.open(f'{path}\{l[i]}')
#     png_image.save(f'{outputpath}\{l[i]}.webp', "webp")