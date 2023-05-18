from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class User(AbstractBaseUser):

    student_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_qut_student = models.BooleanField(default=False)
    university = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['student_number', 'full_name', 'university']
    objects = UserManager()

    def __str__(self):
        return f"{self.full_name} - {self.student_number} - {self.university}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    email = models.EmailField()
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField(null=True, blank=True)

