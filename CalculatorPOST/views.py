from django.shortcuts import render
from CalculatorGET import viewsGET

# Create your views here.

def Home_page(request):
    return render(request, 'homepage.html')

def HomeGET(request):
    return render(request, 'homeGET.html')

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'About.html')

def Calculate(request) :
    Result = 0
    input1 = float(request.POST['X'])
    input2 = float(request.POST['Y'])
    if 'add' in request.POST:
        Result = input1 + input2
    elif 'minus' in request.POST:
        Result = input1 - input2
    elif 'multiple' in request.POST:
        Result = input1 * input2
    elif 'divide' in request.POST:
        Result = input1 / input2
    else :
        Result = 'Please Enter the number!'

    if 'continue' in request.POST:
        input1 = float(Result)
    return render(request, 'home.html',{'Result':Result})