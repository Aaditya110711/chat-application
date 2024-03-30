from django.urls import path
from account.views import (
    login_view,
    logout_view,
    forgot_password_view,
    registeration_view,
    check_otp_view,
    check_reset_otp_view,
    reset_new_password_view,
)

app_name = 'account'  # Define the app namespace

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registeration_view, name='register'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('activate-email/', check_otp_view, name='activate_email'),
    path('reset-code/', check_reset_otp_view, name='reset_code'),
    path('new-password/', reset_new_password_view, name='reset_new_password'),
]
