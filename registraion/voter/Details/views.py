from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializer import UserSerializer,loginSerializer
from django.db.models import Q


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Registration success',
                # 'user_data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginView(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request):
        emailid_or_phonenumber_or_username = request.data.get('emailid')
        password = request.data.get('Password')
        print(emailid_or_phonenumber_or_username)

        matching_registers = User.objects.filter(
            Q(emailid=emailid_or_phonenumber_or_username) | Q(phonenumber=emailid_or_phonenumber_or_username) | Q(username=emailid_or_phonenumber_or_username)
        )

        if matching_registers:
            for user_instance in matching_registers:
                if password == user_instance.Password:
                    return Response({
                        'Message': 'Success',
                        'Result': UserSerializer(user_instance).data,    # this is the show the all Details output when is uncomment details will show you
                        'status': 200
                    })

        return Response({'Message': 'Fail', 'status': 400})




####################this code are single login id when run we can easily understand ###########################


# class LoginView(generics.GenericAPIView):
#     serializer_class = loginSerializer
#
#     def post(self, request):
#         email_id = request.data.get('emailid')
#         password = request.data.get('Password')
#
#
#         matching_registers = User.objects.filter(emailid=email_id)
#         print(matching_registers, "matching")
#
#         if matching_registers:
#             for User_instance in matching_registers:
#                 if password == User_instance.Password:
#                     return Response({'Message': 'Success',
#                                      'Result': UserSerializer(User_instance).data,
#                                      'status': 200})
#         else:
#             return Response({'Message': 'Fail',
#                              'status': 400})


