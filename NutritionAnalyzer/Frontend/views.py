from django.shortcuts import render 
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def home(request):
    return render(request, 'index.html')

# def analyze(request):
#     return render(request, 'Analyze.html')

# def login(request):
#     return render(request, 'login.html')

# def signup(request):
#     return render(request, 'Register.html') 

def analyze(request):
    # You can pass context here if needed, for now, it will just render the page
    return render(request, 'Analyze.html')

def track(request):
    # You can pass context here if needed, for now, it will just render the page
    return render(request, 'Track.html')