from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse('<h1>this is first function in app1 </h1>')

def app1_second(request):
    return HttpResponse('<h1>this is second function in app1 </h1>')


