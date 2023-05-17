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
        srz_email = ForgotPasswordSerializer(data=request.data)
        if srz_email.is_valid():
            email = srz_email.validated_data['email']
            random_code = random.randint(1000, 9999)
            expire_time = timezone.now() + timedelta(minutes=5)
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
            code = OtpCode.objects.filter(email=vd['email'], expire_time__gt=now).order_by('-created_at').first()
            if code:
                if code.code == vd['code']:
                    user = get_object_or_404(User, email=vd['email'])
                    user.password = make_password(vd['new_password'])
                    user.save()
                    OtpCode.objects.filter(email=vd['email']).delete()
                    return Response(data='Your password has been changed correctly', status=status.HTTP_200_OK)
                return Response(data='code is not correct', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data='code is not correct', status=status.HTTP_400_BAD_REQUEST)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
