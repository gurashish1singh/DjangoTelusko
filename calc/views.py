from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h1> Hello World </h1>') # Hard coded
    # return render(request, 'home.html') # Template file
    return render(request,'home.html',{'name': 'Gura'}) # Dynamic content

def summation(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) + int(val2)

    context = {
        'result': res
        }

    return render(request, 'result.html', context)