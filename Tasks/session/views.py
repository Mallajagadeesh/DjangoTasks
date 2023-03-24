from django.shortcuts import render,HttpResponse
from .models import person
from django.http import HttpResponse
# Create your views here.
def games(request):
    if request.method == 'POST':
        d = person()
        d.username = request.POST.get('username')
        d.password = request.POST.get('password')
        d.gender = request.POST.get('gender')
        request.session = ['name']
        d.save()
        return HttpResponse('success')
    else:
        HttpResponse()
        return render(request,'register.html')

def setsession(request):
    request.session['name'] = 'jagadeesh'
    return render(request,'setsession.html')


def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request,'getsession.html',{'name':name})
    else:
        return HttpResponse('your session are expired....')


def login(request):
    if request.method == 'POST':
        Name = request.POST.get('username')
        password = request.POST.get('password')
        u = person.objects.get(username=Name)
        request.session['name'] = u.username
        if u.password == password:
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('wrong details')
    return render(request,'login2.html')