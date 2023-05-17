from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializer import RegisterSerializer
from accounts.models import User


class RegisterView(APIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        srz_data = RegisterSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data['email'], status=status.HTTP_201_CREATED)
        else:
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
