# from rest_framework.views import APIView
# from rest_framework.response import Response 
# from rest_framework.request import Request
# from rest_framework import status
# from library.lib.services.user_service import register_user
# from library.lib.serializers.serializer import UserSerializer


# class RegisterUser(APIView):
    
#     def post(self, request: Request) -> Response:
#         serializer  = UserSerializer(data = request.data)

#         if serializer.is_valid():
#             user = register_user(serializer.validated_data)           
#             return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)