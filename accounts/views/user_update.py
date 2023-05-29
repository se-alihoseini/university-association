from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializer import UserSerializer


class UserUpdate(APIView):
    serializer_class = UserSerializer

    def put(self, request):
        user = request.user
        srz_data = UserSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
