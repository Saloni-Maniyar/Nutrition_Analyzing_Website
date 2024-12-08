from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def analyze(request):
    return render(request, 'Analyze.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'Register.html')