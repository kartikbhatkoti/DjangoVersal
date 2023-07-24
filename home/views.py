from django.shortcuts import render, HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('Welcome to this website')

# def index(request):
#     return render(request, 'index.html')


def index(request):
    context = {
        'variable1' : 'Some variable content sent to index.html',
        'variable2' : 'Another variable content sent to index.html'
    }
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse('Welcome to this about page')

def contact(request):
    return HttpResponse('Welcome to this conact page')

def services(request):
    return HttpResponse('Welcome to this services page')

