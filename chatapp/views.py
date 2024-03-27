from django.shortcuts import render

# Create your views here.

def index(request):
    contex = {}
    return render(request, "chatapp/index.html", contex)
