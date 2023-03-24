from django.shortcuts import render
from .models import images
from django.http import HttpResponse
# Create your views here.
def upload(request):
    if request.method == 'POST':
        a = images()
        a.Name = request.POST.get('Name')
        a.images = request.FILES['images']
        a.save()
        return HttpResponse('uploaded')
    return render(request,'images.html')