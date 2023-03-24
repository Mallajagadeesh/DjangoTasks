import base64


def img(images):
    img = open('/home/madhu/PycharmProjects/pythonProject1/photos/images/images/download.jpeg')
    data = base64.b64encode(images.read())
    return data