from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token, RefreshToken
from django.contrib.auth import login, authenticate
from accounts.serializer import LoginSerializer
from accounts.models import User
from django.shortcuts import get_object_or_404


class LoginView(APIView):

    serializer_class = LoginSerializer

    def post(self, request):
        srz_data = LoginSerializer(data=request.data)
        if srz_data.is_valid():
            vd = srz_data.validated_data
            user = authenticate(request, email=vd['email'], password=vd['password'])
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access = str(refresh.access_token)
                return Response({'access': access, 'refresh': str(refresh), 'user': user.email}, status=status.HTTP_200_OK)
            else:
                return Response('user does not exist', status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
