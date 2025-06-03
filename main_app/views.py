from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Backpacking Blueprint</h1>')

def discover(request):
    return render(request, 'discover.html')