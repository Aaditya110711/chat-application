from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    user =  request.user.profile
    friends = user.friends.all()
    contex = {
        "user" : user,
        "friends" : friends
    }
    return render(request, "chatapp/index.html", contex)

@login_required
def friend(request,id):
    context = {}
    return render(request , "chatapp/chatbox.html", context)
