from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from chatapp.models import (Friend, ChatMessage)
from django.contrib.auth.models import User
# Create your views here.

@login_required
def index(request):
    user = request.user.profile
    user_friends = user.friends.all()
    contex = {
        "user": user,
        "user_friends": user_friends
    }
    return render(request, "chatapp/index.html", contex)

@login_required
@csrf_exempt
def friend(request,id):
    user = request.user.profile
    user_friends = user.friends.all()
    friend = Friend.objects.get(profile_id=id)

    chats = ChatMessage.objects.filter(
        msg_sender=user, msg_receiver=friend.profile).values()

    context = {
        "user_friends": user_friends,
        "friend": friend,
        "room_name" : "test"
    }
    return render(request, "chatapp/chatbox.html", context)
