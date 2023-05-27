from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    student_number = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='image/user/', null=True, blank=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_qut_student = models.BooleanField(default=False)
    university = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['student_number', 'full_name', 'university']
    objects = UserManager()

    def __str__(self):
        return f"{self.full_name} - {self.student_number} - {self.university}"


    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField(null=True, blank=True)

