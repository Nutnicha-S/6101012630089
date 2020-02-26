from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'home.html')

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
    return render(request, 'home.html',{'Result':Result})