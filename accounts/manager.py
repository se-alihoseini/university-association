from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, full_name, student_number, university, password):
        if not email:
            raise ValueError('email field is required')
        if not full_name:
            raise ValueError('full_name field is required')
        if not student_number:
            raise ValueError('student number field is required')
        if not university:
            raise ValueError('university field is required')
        if not password:
            raise ValueError('password field is required')

        user = self.model(email=self.normalize_email(email), full_name=full_name, student_number=student_number,
                          university=university)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, student_number, university, password):
        user =self.create_user(email, full_name, student_number, university, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
