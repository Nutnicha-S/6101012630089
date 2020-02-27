from django.shortcuts import render

# Create your views here.
def HomeGET(request):
    return render(request, 'homeGET.html')