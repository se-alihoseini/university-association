from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import logout


class LogoutView(APIView):

    # permission_classes = [IsAuthenticated, ]

    def get(self, request):
        logout(request)
        return Response('your logout', status=status.HTTP_200_OK)
