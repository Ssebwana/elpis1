from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')
def about(request):
    return render(request, 'main/about.html')


def programs(request):
    return render(request, 'main/programs.html')


def partnerships(request):
    return render(request, 'main/partnerships.html')


def donate(request):
    return render(request, 'main/donate.html')


def contact(request):
    return render(request, 'main/contact.html')