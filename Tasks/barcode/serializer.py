import base64
from .bar import logic
from .models import barcode
from rest_framework import serializers
class barcodeserializer(serializers.ModelSerializer):
    class Meta:
        model = barcode
        fields = '__all__'


    def create(self,validated_date):
        product_name = validated_date['product_name']
        product_code = validated_date['product_code']
        pack_code = validated_date['pack_code']
        code_genaration = product_code+' '+pack_code
        combined = logic(code_genaration,product_name)
        with open(combined,'rb') as img:
            encoded = base64.b64encoded(img.read())
            print(encoded)
            pos = barcode.objects.create(product_namer=product_name,product_code=product_code,pack_code=pack_code,br_code = encoded)
            pos.save()
            return pos

