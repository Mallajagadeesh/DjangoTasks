from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializer import registerserializer, Loginserializer
from django.http import HttpResponse
from rest_framework import status


class Registration(generics.GenericAPIView):
    serializer_class = registerserializer

    def post(self, request):
        # Deserialize the request data using your serializer
        serializer = self.get_serializer(data=request.data)

        # Check if the data is valid
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check if a user with the same email already exists
        email_id = serializer.validated_data.get('email_id')
        existing_user = register.objects.filter(email_id=email_id).first()
        if existing_user:
            return Response({'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        serializer.save()

        return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)


#
# class Registration(generics.GenericAPIView):
#     serializer_class = registerserializer
#
#     def post(self, request):
#         # Deserialize the request data using your serializer
#         serializer = self.get_serializer(data=request.data)
#
#         # Check if the data is valid
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         # Check if a user with the same email already exists
#         email_id = serializer.validated_data.get('email_id')
#         existing_user = register.objects.filter(email_id=email_id).first()
#         if existing_user:
#             return Response({'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # Create a new user
#         serializer.save()
#
#         return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)
#

class Registration(generics.GenericAPIView):
    serializer_class = registerserializer

    def post(self, request):
        # Extract data from the request
        full_name = request.data.get('fullName')
        email_id = request.data.get('email_id')
        password = request.data.get('Password')  # Use lowercase for consistency
        address = request.data.get('address')

        # Check if a user with the same email already exists
        existing_user = register.objects.filter(email_id=email_id).first()
        if existing_user:
            return Response({'message': 'Email already exists'}, status=400)

        # Create a new user
        new_user = register(fullName=full_name, email_id=email_id, Password=password, address=address)
        new_user.save()

        return Response({'message': 'Success'}, status=200)





#
# class login(generics.GenericAPIView):
#     serializer_class = Loginserializer
#
#     def post(self, request):
#         email_id = request.data.get('email_id')
#         Password = request.data.get('Password')
#         l = register.objects.get(email_id=email_id)
#         if Password == l.Password:
#             # print("dfghj")
#             return Response({'Message': 'Success',
#                              'Result': Loginserializer(l).data,
#                              'status': 200})
#         else:
#             # print("else")
#             return Response({'Message': 'Fail',
#                              'status': 400})


class Login(generics.GenericAPIView):
    serializer_class = Loginserializer

    def post(self, request):
        email_id = request.data.get('email_id')
        password = request.data.get('Password')  # Use lowercase for consistency

        # Add debugging print statements
        print('Received email_id:', email_id)
        print('Received password:', password)

        # Use filter instead of get to retrieve all matching records
        matching_registers = register.objects.filter(email_id=email_id)
        print(matching_registers, "matching")

        # Check if there are any matching records
        if matching_registers:
            # Loop through the matching records or apply further filtering
            for register_instance in matching_registers:
                if password == register_instance.Password:
                    return Response({'Message': 'Success',
                                     'Result': registerserializer(register_instance).data,
                                     'status': 200})
        else:
            return Response({'Message': 'Fail',
                             'status': 400})
