from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import RegisterLoginView, LoginUserVerifyCodeView, RegisterUserVerifyCodeView, UserLogoutView


class TestUrl(TestCase):
    def test_register_login(self):
        url = reverse('accounts:register_login')
        self.assertEqual(resolve(url).func.view_class, RegisterLoginView)

    def test_login_verify(self):
        url = reverse('accounts:login_verify')
        self.assertEqual(resolve(url).func.view_class, LoginUserVerifyCodeView)

    def test_register_verify(self):
        url = reverse('accounts:register_verify')
        self.assertEqual(resolve(url).func.view_class, RegisterUserVerifyCodeView)

    def test_logout(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class, UserLogoutView)
