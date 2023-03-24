import base64

from django.shortcuts import render
from .models import covert
from django.http import HttpResponse
# Create your views here.
def images (request):
    if request.method == 'POST':
        a = covert()
        a.Name = request.POST.get('Name')
        images = request.FILES['images']
        print(images)
        images = str(images)
        img = open('/home/madhu/PycharmProjects/pythonProject1/photos/images/images/download.jpeg','rb')

        base = base64.b64encode(img.read())
        # print(base)
        a.images = base
        print(a.images)
        a.save()
        return HttpResponse('SUCCESSS')
    return render(request,'base64.html')

