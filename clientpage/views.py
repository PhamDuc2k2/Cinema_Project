from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .middlewares import auth, guest
# Create your views here.

@guest
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        initial_data = {'username':'', 'password1':'', 'password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form': form})

@guest
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        initial_data = {'username':'', 'password1':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form': form})

@auth
def home_view(request):
    user = request.user
    account = user.account_user
    return render(request, 'home.html', {'user': user, 'account': account})

def logout_view(request):
    logout(request)
    return redirect('login')

@auth
def info_user_view(request):
    user = request.user
    account = user.account_user

    if request.method == 'POST':
            # Lấy giá trị từ form
            username = request.POST['username']
            email = request.POST['email']

            receive_announcement = request.POST.get('receive_announcement', 'no')
            status = receive_announcement == "yes"

            # Lưu giá trị vào cơ sở dữ liệu
            user.username = username
            user.email = email
            account.receive_announcement = status

            # Lưu thay đổi
            user.save()
            account.save()

    return render(request, 'info_user.html', {'user':user, 'account': account})