from django.shortcuts import render,redirect
from account.decorators import only_authenticated_user, redirect_authenticated_user
from account.forms import *
from django.contrib.auth import (authenticate,get_user_model,login,logout,)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.crypto import get_random_string
from account.utils import (
    send_activation_code,
    send_reset_password_code,
)
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your views here.


@redirect_authenticated_user
def login_view(request):
    error = None
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['username_or_email'], password=form.cleaned_data['password'])
            if user:
                if not user.is_active:
                    messages.warning(request, _(
                        f"It's look like you haven't still verify your email - {user.email}"))
                    return redirect('users:activate_email')
                else:
                    login(request, user)
                    return redirect('chatapp:chat')
            else:
                error = 'Invalid Credentials'
    else:
        form = CustomLoginForm()
    return render(request, 'account/login.html', {'form': form, 'error': error})


@only_authenticated_user
@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login')


@redirect_authenticated_user
def registeration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.source = 'Register'
            user.save(True)

            code = get_random_string(20)
            otp = OtpCode(code=code, user=user)
            otp.save(True)
            try:
                send_activation_code(user.email, code)
            except:
                otp.delete()
                user.delete()
                messages.error(request, _('Failed while sending code!'))
            else:
                messages.success(
                    request, _(f'We have sent a verification code to your email - {user.email}'))
                return redirect('users:activate_email')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


@redirect_authenticated_user
def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgetPasswordEmailCodeForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            user = get_user_model().objects.get(**username_or_email)
            code = get_random_string(20)
            otp = OtpCode(code=code, user=user, email=user.email)
            otp.save()

            try:
                send_reset_password_code(user.email, code)
            except Exception as e:
                otp.delete()
                messages.error(request, _('Failed while sending code!'))
            else:
                messages.success(request, _(
                    f"We've sent a passwrod reset otp to your email - {user.email}"))
                return redirect('users:reset_code')
    else:
        form = ForgetPasswordEmailCodeForm()
    return render(request, 'account/forgot_password.html', context={'form': form})

@redirect_authenticated_user
def check_otp_view(request):
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = OtpCode.objects.get(code=form.cleaned_data['otp'])
            user = otp.user
            otp.delete()
            user.is_active = True
            user.save()
            return redirect('users:login')
    else:
        form = OtpForm()
    return render(request, 'account/user_otp.html', {'form': form})

@redirect_authenticated_user
def check_reset_otp_view(request):
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = OtpCode.objects.get(code=form.cleaned_data['otp'])
            request.session['email'] = otp.user.email
            messages.success(request, _(
                "Please create a new password that you don't use on any other site."))
            return redirect('users:reset_new_password')
    else:
        form = OtpForm()
    return render(request, 'account/user_otp.html', {'form': form})


@redirect_authenticated_user
def reset_new_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            email = request.session['email']
            del request.session['email']
            user = User.objects.get(email=email)
            user.password = make_password(form.cleaned_data["new_password2"])
            user.save()
            messages.success(request, _(
                "Your password changed. Now you can login with your new password."))
            return redirect('users:login')
    else:
        form = ChangePasswordForm()
    return render(request, 'account/new_password.html', {'form': form})