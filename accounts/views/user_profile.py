from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.serializer import UserSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        srz_data = UserSerializer(instance=user)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
