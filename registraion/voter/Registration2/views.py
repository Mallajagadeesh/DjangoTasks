from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import UserRegister,loginRegister
from .models import RegisterUser
from django.db.models import Q



class Register2View(generics.GenericAPIView):
    serializer_class = UserRegister

    def post(self, request):
        serializer = UserRegister(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Registration success',
                'user_data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(generics.GenericAPIView):
    serializer_class = loginRegister

    def post(self, request):
        emailid_or_phonenumber_or_username = request.data.get('emailid')
        password = request.data.get('Password')
        print(emailid_or_phonenumber_or_username)

        matching_registers = RegisterUser.objects.filter(
            Q(emailid=emailid_or_phonenumber_or_username) | Q(phonenumber=emailid_or_phonenumber_or_username) | Q(username=emailid_or_phonenumber_or_username)
        )

        if matching_registers:
            for user_instance in matching_registers:
                if password == user_instance.Password:
                    return Response({
                        'Message': 'Success',
                        'Result': UserRegister(user_instance).data,     ################ this is the show the all Details output when is uncomment details will show you
                        'status': 200
                    })

        return Response({'Message': 'Fail', 'status': 400})


####################this code are single login id when run we can easily understand ###########################
#
# class LoginView(generics.GenericAPIView):
#     serializer_class = loginRegister
#
#     def post(self, request):
#         email_id = request.data.get('emailid')
#         password = request.data.get('Password')
#
#         matching_registers = RegisterUser.objects.filter(emailid=email_id)
#         print(matching_registers, "matching")
#
#         if matching_registers:
#             for User_instance in matching_registers:
#                 if password == User_instance.Password:
#                     return Response({'Message': 'Success',
#                                      'Result': UserRegister(User_instance).data,
#                                      'status': 200})
#         else:
#             return Response({'Message': 'Fail',
#                              'status': 400})
#
