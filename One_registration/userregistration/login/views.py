from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from .models import Registration


class Register2View(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Registration success',
                'user_data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#################### This code use of email and username deatails is given login success    ######################
class LoginView(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request):
        email_or_username = request.data.get('Email_id')  # Assuming Email_id can be either email or username
        password = request.data.get('password')

        # Check if the input is an email or username
        is_email = '@' in email_or_username

        if is_email:
            matching_registers = Registration.objects.filter(Email_id=email_or_username)
        else:
            matching_registers = Registration.objects.filter(username=email_or_username)

        if matching_registers:
            for user_instance in matching_registers:
                if password == user_instance.password:
                    return Response({'Message': 'Success',
                                     'Result': UserSerializer(user_instance).data,
                                     'status': 200})
            # Password didn't match for any user instance
            return Response({'Message': 'Password did not match', 'status': 400})
        else:
            return Response({'Message': 'User not found', 'status': 400})







#
# ##################### This single email and password given this code use ################################
#
# class LoginView(generics.GenericAPIView):
#     serializer_class = loginSerializer
#
#     def post(self, request):
#         email_id = request.data.get('Email_id')
#         Password = request.data.get('password')
#         matching_registers = Registration.objects.filter(Email_id=email_id)
#
#         if matching_registers:
#             for user_instance in matching_registers:
#                 if Password == user_instance.password:
#                     return Response({'Message': 'Success',
#                                      'Result': UserSerializer(user_instance).data,
#                                      'status': 200})
#             # Password didn't match for any user instance
#             return Response({'Message': 'Password did not match', 'status': 400})
#         else:
#             return Response({'Message': 'Fail', 'status': 400})




