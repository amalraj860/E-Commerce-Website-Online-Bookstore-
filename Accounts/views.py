from django.shortcuts import render, redirect
from .models import User
from django.http import HttpRequest


# Create your views here.
def Login(requests):
    if requests.method == "POST":
        user_name1 = requests.POST.get('username')
        user_pass = requests.POST.get("password")
        user_check = User.objects.filter(email=user_name1, password=user_pass).values()

        print(user_check)

        if user_check:
            requests.session['s_name'] = user_name1
            k = User.objects.get(email=user_name1)
            print(k)
            name1 = k.user_name.upper()
            print(name1)
            return render(requests, 'home.html', {'name2': name1})
        else:
            return render(requests, 'login.html',{'status': 'invalid'})
    return render(requests, 'login.html')


def Register(requests):
    if requests.method == "POST":
        user_name1 = requests.POST.get('username')
        user_email = requests.POST.get('email')
        user_password = requests.POST.get('password')
        reg_var = User()
        reg_var.user_name = user_name1
        reg_var.email = user_email
        reg_var.password = user_password
        reg_var.save()
        return redirect('/')

    return render(requests, 'register.html')



# function for user logout
def Logout(request):
    try:
        del request.session['s_name']
        return redirect('/')
    except:
        return redirect('/')




