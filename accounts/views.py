from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.

def home(request):
    """홈 페이지"""
    return render(request, 'accounts/home.html')

def user_login(request):
    """사용자 로그인"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username}님, 환영합니다!')
                return redirect('home')
            else:
                messages.error(request, '사용자명 또는 비밀번호가 올바르지 않습니다.')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def user_register(request):
    """사용자 회원가입"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '회원가입이 완료되었습니다!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def user_logout(request):
    """사용자 로그아웃"""
    logout(request)
    messages.info(request, '로그아웃되었습니다.')
    return redirect('login')

@login_required
def profile(request):
    """사용자 프로필"""
    return render(request, 'accounts/profile.html')
