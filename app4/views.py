from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse('<h2>this is first functin of app2</h1>')
def app2_second(request):
    return HttpResponse('<h2>this is second functin of app2</h1>')

