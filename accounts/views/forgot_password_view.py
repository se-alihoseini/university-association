from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import string
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from accounts.serializer import ForgotPasswordSerializer, ChangePasswordSerializer
from accounts.models import User, OtpCode
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail


def get_random_string(length):
    # choose from all lowercase letter
    characters = string.ascii_letters + string.digits + string.punctuation
    # letters = string.printable
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str


class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        user = request.user
        random_code = get_random_string(8)
        expire_time = timezone.now() + timedelta(minutes=5)
        if request.user.is_authenticated:
            email = user.email
            OtpCode.objects.filter(email=email).delete()
            OtpCode.objects.create(email=email, code=random_code, expire_time=expire_time)
            send_mail('Password Reset', 'Your verification code: %s' % (random_code,), 'csco.tech <support@mail.csco.tech>',
                      [email], fail_silently=False)
            return Response({"success": "OTP code sent successfully"}, status=status.HTTP_200_OK)
        else:
            srz_email = ForgotPasswordSerializer(data=request.data)
            if srz_email.is_valid():
                email = srz_email.validated_data['email']
                OtpCode.objects.filter(email=email).delete()
                OtpCode.objects.create(email=email, code=random_code, expire_time=expire_time)
                send_mail('Password Reset', 'Your verification code: %s' % (random_code,), 'csco.tech <support@mail.csco.tech>',
                          [email], fail_silently=False)
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
            otp_code = OtpCode.objects.get(email=email, expire_time__gt=now)
            if otp_code:
                if otp_code.code == vd['code']:
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


# pensive_mayer_8ulrkt
# 6c6d1729-7771-4a0b-97e6-0ee925f3f332