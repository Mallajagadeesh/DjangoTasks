from django.shortcuts import render,HttpResponse
from .models import sessionlogin
from django.http import HttpResponse
# Create your views here.
def robo(request):
    if request.method == 'POST':
        d=sessionlogin()
        d.username = request.POST.get('username')
        d.password = request.POST.get('password')
        d.gender = request.POST.get('gender')
        request.session = ['name']
        d.save()
        return HttpResponse('SUCCESS')
    else:
        HttpResponse()
        return render(request,'register2.html')


def setsession(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = sessionlogin.objects.get(username=username)
        print(u)
        request.session['name'] = u.username
        request.session.set_expiry(30)
        if u.password == password:
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('wrong details')
    return render(request,'login3.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        return render(request,'getsession.html',{'name':name})
    else:
        return HttpResponse('your session are expired')
