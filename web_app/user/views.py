from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'user/login.html', {'title': 'Login'})

def register(request):
    return render(request, 'user/register.html', {'title': 'Register'})
