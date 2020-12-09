from django.shortcuts import render
# from django.http import HttpResponse


def home(request):

    return render(request, 'blogapp/home.html')
    # return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return render(request, 'blogapp/about.html')
    # return HttpResponse('<p>Its me. ya boi</p>')
