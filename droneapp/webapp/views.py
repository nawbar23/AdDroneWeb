from django.shortcuts import render

def index(request):
    return render(request, 'webapp/home.html')

def history(request):
    return render(request, 'webapp/history.html')

def adds(request):
    return render(request, 'webapp/adds.html')
