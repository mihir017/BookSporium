from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.models import Users, BookstoreSeller, MessageByChat
from posts.models import BookAd
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from users.serializers import MessageSerializer, UserSerializer

# Create your views here.
def sellerChatBox(request,reciever_id):
    receiver = BookAd.objects.get(id = reciever_id)
    sender = Users.objects.get(email = request.session.get("email"))
    return render(request,"post/chat_app.html",{"seller_detail": receiver,"sender_detail": sender,'messages': MessageByChat.objects.filter(sender=sender, receiver=receiver.seller) | MessageByChat.objects.filter(sender=receiver.seller, receiver=sender)})


# @csrf_exempt
# def message_list(request,sender = None,receiver = None):
    # receiver = BookAd.objects.get(id = receiver_id)
    # sender = Users.objects.get(email = request.session.get("email"))
    # if request.method == 'GET':
    #     messages = MessageByChat.objects.filter(sender=sender, receiver=receiver, is_read=False)
    #     serializer = MessageSerializer(messages, many=True, context={'request': request})
    #     for message in messages:
    #         message.is_read = True
    #         message.save()
    #     return JsonResponse(serializer.data, safe=False)

    # if request.method == 'POST':
        # msg = {
        #     "sender" : sender,
        #     "receiver" : receiver.seller,
        #     "message" : request.POST.get("message")
        # }
        # MessageByChat.objects.create(**msg)
        # print(request.POST.get("message"))
        # return redirect("chat_box")

        # data = JSONParser().parse(request)
        # print(data)
        # print("*********")
        # serializer = MessageSerializer(data=data)
        # print(serializer.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)

def message_list(request,reciever_id):
    sender = Users.objects.get(email = request.session.get("email"))
    receiver = BookAd.objects.get(id = reciever_id)
    if request.method == "POST":
        print(request.POST.get("message"))
        msg = {
            "sender" : sender,
            "receiver" : receiver.seller,
            "message" : request.POST.get("message")
        }
        MessageByChat.objects.create(**msg)
        params = {"seller_detail": receiver,"sender_detail": sender,"messages":MessageByChat.objects.filter(sender=sender, receiver=receiver.seller) | MessageByChat.objects.filter(sender=receiver.seller, receiver=sender)}
        # sellerChatBox(request,reciever_id)
        # return redirect("message_show")
        # return redirect("url 'chat' reciever_id")
        # message_show(request,receiver,sender)
        return render(request,"post/chat_app.html",params)


# def chat_view(request):
#     if not request.user.is_authenticated:
#         return redirect('index')
#     if request.method == "GET":
#         return render(request, 'chat/chat.html',
#                       {'users': Users.objects.exclude(email=request.user.username)})


# def message_view(request, sender, receiver):
#     if not request.user.is_authenticated:
#         return redirect('index')
#     if request.method == "GET":
#         return render(request, "chat/messages.html",
#                       {'users': User.objects.exclude(username=request.user.username),
#                        'receiver': User.objects.get(id=receiver),
#                        'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
#                                    Message.objects.filter(sender_id=receiver, receiver_id=sender)})
