import base64
import pyqrcode
from django.shortcuts import render
from rest_framework import serializers,request
from .models import qrcode
#from barcode_generator.bar import logic

class qrserializer(serializers.ModelSerializer):
    class Meta:
        model = qrcode
        fields = ['product_namer','product_code','pack_code']

    def create(self,validated_date):
        product_namer = validated_date['product_namer']
        product_code = validated_date['product_code']
        pack_code = validated_date['pack_code']
        a = product_code+""+pack_code
        b = pyqrcode.create(a)
        b.png(f'{product_namer}.png',scale=6)
        with open('/home/madhu/Downloads/download.jpeg',"rb")as img:
            encoded=base64.b64encode(img.read())
            pos = qrcode.objects.create(product_namer=product_namer,product_code=product_code,pack_code=pack_code,qr_code=encoded)
            pos.save()
            return pos

    # def getimage(self,requset):
    #     products = qrcode.objects.all()
    #     return render(request,'index.html',{'qr_code':products})
