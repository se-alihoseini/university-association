from django.urls import path
from accounts.views import register_view, login_view, logout_view, forgot_password_view

app_name = 'accounts'
urlpatterns = [
    path('register/', register_view.RegisterView.as_view(), name='user_register'),
    path('login/', login_view.LoginView.as_view(), name='user_login'),
    path('logout/', logout_view.LogoutView.as_view(), name='user_logout'),
    path('forgot_password/', forgot_password_view.ForgotPasswordView.as_view(), name='forgot_password'),
    path('change_password/', forgot_password_view.ChangePasswordView.as_view(), name='change_password'),
]
