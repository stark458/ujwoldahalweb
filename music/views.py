from django.shortcuts import render
from django.http import HttpResponse

"""def begin(request):
    return HttpResponse("Hello, world. This is music.")"""

def index(request):
    return render(request,'music/music.html')

