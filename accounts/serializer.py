from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer
from rest_framework import status
from .models import User, OtpCode

from django.contrib.auth.hashers import make_password


class RegisterSerializer(ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'student_number', 'university', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        del validated_data['confirm_password']
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password doesnt match')
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)
    code = serializers.IntegerField()
    email = serializers.EmailField(required=False)

    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError('password doesnt match')
        return data
