from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from accounts.models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


# after Sign In Function
def afterSignin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            Users.objects.get(email = email)
        except Exception as err:
            msg = "Email and Password is Wrong.."
            return render(request,"accounts/signin.html",{"error_msg": msg})
        else:
            user = Users.objects.get(email = email)
            if(user.password == request.POST.get("password")):
                # return HttpResponse("SuccessFully LogIn...")
                # return render(request,"post/home.html")
                return homePage(request)
            else:
                msg = "Email and Password is Wrong.."
                return render(request,"accounts/signin.html",{"error_msg": msg})

# home Page
def homePage(request):
    if request.session.get("email"):
        return render(request,"post/home.html")

# create Book Post Ad
def postBookAD(request):
    return render(request,"post/post_book.html")

def submitPost(request):
    if request.method == "POST":
        book_detail = {
            "seller": Users.objects.get(email = request.session.get("email")),
            "book_name": request.POST.get("book_name"),
            "book_author": request.POST.get("book_author_name"),
            "book_price": float(request.POST.get("book_price")),
            "description": request.POST.get("book_desc"),
            "image_1": request.POST.get("image_1"),
            "image_2": request.POST.get("image_2"),
            "image_3": request.POST.get("image_3"),
            "state": request.POST.get("state"),
            "city": request.POST.get("city"),
            "area": request.POST.get("area")
        }
        print(book_detail)
        BookAd.objects.create(**book_detail)
        # return render(request,"post/home.html")
        return redirect("homePage")