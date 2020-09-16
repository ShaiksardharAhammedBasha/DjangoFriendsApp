from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    test = 'Testing Page'
    context = {
        'user' : user,
        'test' : test,
    }
    return render(request, 'main/home.html', context)