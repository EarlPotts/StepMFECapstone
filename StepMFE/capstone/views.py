from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'capstone/index.html')
    
def history(request):
    return render(request, 'capstone/history-page.html')

def invest(request):
    return render(request, 'capstone/invest-page.html')