from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import random

from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from accounts.serializer import ForgotPasswordSerializer, ChangePasswordSerializer
from accounts.models import User, OtpCode
from django.contrib.auth.hashers import make_password


class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        user = request.user
        random_code = random.randint(1000, 9999)
        expire_time = timezone.now() + timedelta(minutes=5)
        if request.user.is_authenticated:
            email = user.email
            OtpCode.objects.filter(email=email).delete()
            OtpCode.objects.create(email=email, code=random_code, expire_time=expire_time)
            return Response({"success": "OTP code sent successfully"}, status=status.HTTP_200_OK)
        else:
            srz_email = ForgotPasswordSerializer(data=request.data)
            if srz_email.is_valid():
                email = srz_email.validated_data['email']
                OtpCode.objects.filter(email=email).delete()
                OtpCode.objects.create(email=email, code=random_code, expire_time=expire_time)
                return Response({"success": "OTP code sent successfully"}, status=status.HTTP_200_OK)
            return Response(srz_email.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        srz_data = ChangePasswordSerializer(data=request.data)
        if srz_data.is_valid():
            vd = srz_data.validated_data
            now = timezone.now()
            if request.user.is_authenticated:
                email = request.user.email
            else:
                email = vd['email']
            code = OtpCode.objects.filter(email=email, expire_time__gt=now)
            if code:
                if code.code == vd['code']:
                    if request.user.is_authenticated:
                        user = request.user
                    else:
                        user = get_object_or_404(User, email=email)
                    user.password = make_password(vd['new_password'])
                    user.save()
                    OtpCode.objects.filter(email=email).delete()
                    return Response(data='Your password has been changed correctly', status=status.HTTP_200_OK)
                return Response(data='code is not correct', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data='code is not correct', status=status.HTTP_400_BAD_REQUEST)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
