from django.shortcuts import render
def loginpage(request):
    return render(request, 'pro/login.html')
