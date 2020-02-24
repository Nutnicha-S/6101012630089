from django.shortcuts import render, redirect

# Create your views here.

def calculator(request):
    return render(request, 'home.html')