from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Users, BookstoreSeller, BookStoreAd, MessageByChat, UserImage
from posts.models import BookAd
from e_book.models import EBook
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# Home Function
def home(request):
    if request.session.get('email'):
        return redirect("homePage")
    else:
        # return HttpResponse("Booksporium")
        # return redirect("home")
        bookAd_obj = BookAd.objects.all()
        eBook_obj = EBook.objects.all()
        bookStore_obj = BookStoreAd.objects.all()
        for i in eBook_obj:
            i.eBook_name = i.eBook_name.split(":")[0]
        return render(request,"accounts/main.html",{"bookAds":bookAd_obj,"eBooks": eBook_obj,"bookStoreAds":bookStore_obj})

# sign in function
def signin(request):
    if request.session.get('email'):
        if request.session.get('email') == Users.objects.get(email = request.session.get('email')):
            return redirect("homePage")
        elif request.session.get('email') == BookstoreSeller.objects.get(email = request.session.get('email')):
            return redirect("seller_homePage")
    else:
        return render(request,"accounts/signin.html")

# sign Up function
def signup(request):
    return render(request,"accounts/signup.html")

# BookStore signup
def storeSignup(request):
    return render(request,"accounts/book_store_signup.html")

# afterSignUp function
def afterSignup(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("ph_number")
        try:
            Users.objects.get(email = request.POST.get("email"))
        except Exception as err:
            if len(request.POST.get("password")) > 7:
                u_letter,l_letter,n_letter,s_char = 0,0,0,0
                for letter in (request.POST.get("password")):
                    if letter.isupper():
                        u_letter += 1  
                    elif letter.islower():
                        l_letter += 1  
                    elif letter.isnumeric():
                        n_letter += 1
                    elif letter in "<>?@#$%&*()!":
                        s_char += 1
                if (u_letter > 0) and (l_letter > 0) and (n_letter > 0) and (s_char > 0):
                    if (len(request.POST.get("ph_number")) > 9):
                        data = {
                            "full_name" : full_name,
                            "email" : request.POST.get("email"),
                            "password" : request.POST.get("password"),
                            "phone_no" : phone_number
                        }
                        # print(type(data["phone_no"]))
                        Users.objects.create(**data)
                        return redirect("signin")
                    else:
                        msg = "Enter Correcrt Phone Number.."
                        return render(request,"accounts/signup.html",{"phone_msg": msg})
                else:
                    msg = "Password Contain must be one Upper,Lower, Numeric and Special Chaacter.."
                    return render(request,"accounts/signup.html",{"password_msg": msg})
            else:
                msg = "Password Contain more then 7 character.."
                return render(request,"accounts/signup.html",{"password_msg": msg})
        else:
            msg = "Email is already Exists..."
            return render(request,"accounts/signup.html",{"email_msg":msg})

# after book Store Sign up
def afterBookStoreSignup(request):
    if request.method == "POST":
        # number = [1020,1019,1018,1017,1016,1015,1014,1013,1012,1011,1010,1009,1008,1007,1006,1005,1004,1003,1002,1001]
        store_name = request.POST.get("store_name")
        seller_name = request.POST.get("seller_name")
        phone_number = request.POST.get("ph_number")
        try:
            BookstoreSeller.objects.get(email = request.POST.get("email"))
        except Exception as err:
            if len(request.POST.get("password")) > 7:
                u_letter,l_letter,n_letter,s_char = 0,0,0,0
                for letter in (request.POST.get("password")):
                    if letter.isupper():
                        u_letter += 1  
                    elif letter.islower():
                        l_letter += 1  
                    elif letter.isnumeric():
                        n_letter += 1
                    elif letter in "<>?@#$%&*()!":
                        s_char += 1
                if (u_letter > 0) and (l_letter > 0) and (n_letter > 0) and (s_char > 0):
                    if (len(request.POST.get("ph_number")) > 9):
                        data = {
                            "store_name" : store_name,
                            "seller_name" : seller_name,
                            "email" : request.POST.get("email"),
                            "password" : request.POST.get("password"),
                            "phone_no" : phone_number
                        }
                        # print(type(data["phone_no"]))
                        BookstoreSeller.objects.create(**data)
                        return redirect("signin")
                    else:
                        msg = "Enter Correcrt Phone Number.."
                        return render(request,"accounts/book_store_signup.html",{"phone_msg": msg})
                else:
                    msg = "Password Contain must be one Upper,Lower, Numeric and Special Chaacter.."
                    return render(request,"accounts/book_store_signup.html",{"password_msg": msg})
            else:
                msg = "Password Contain more then 7 character.."
                return render(request,"accounts/book_store_signup.html",{"password_msg": msg})
        else:
            msg = "Email is already Exists..."
            return render(request,"accounts/book_store_signup.html",{"email_msg":msg})

# after Sign In Function
def afterSignin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            Users.objects.get(email = email)
        except Exception as err:
            try:
                BookstoreSeller.objects.get(email = email)
            except Exception as err:
                msg = "Email and Password is Wrong.."
                return render(request,"accounts/signin.html",{"error_msg": msg})
            else:
                seller = BookstoreSeller.objects.get(email = email)
                if(seller.password == request.POST.get("password")):
                    # return HttpResponse("SuccessFully LogIn...")    
                    request.session['email'] = email
                    request.session['islogin'] = 'true'
                    return render(request,"seller/home_page.html")
                else:
                    msg = "Email and Password is Wrong.."
                    return render(request,"accounts/signin.html",{"error_msg": msg})    
        else:
            user = Users.objects.get(email = email)
            if(user.password == request.POST.get("password")):
                # return HttpResponse("SuccessFully LogIn...")    
                bookAd_obj = BookAd.objects.all()
                eBook_obj = EBook.objects.all() 
                bookStore_obj = BookStoreAd.objects.all()
                request.session['email'] = email
                request.session['islogin'] = 'true'
                for i in eBook_obj:
                    i.eBook_name = i.eBook_name.split(":")[0]
                return render(request,"post/home.html",{"bookAds":bookAd_obj,"eBooks": eBook_obj,"bookStoreAds":bookStore_obj})

            else:
                msg = "Email and Password is Wrong.."
                return render(request,"accounts/signin.html",{"error_msg": msg})

def homePage(request):
    bookAd_obj = BookAd.objects.all()
    eBook_obj = EBook.objects.all()
    bookStore_obj = BookStoreAd.objects.all()
    for i in eBook_obj:
        i.eBook_name = i.eBook_name.split(":")[0]
    print(eBook_obj)
    return render(request,"post/home.html",{"bookAds":bookAd_obj,"eBooks": eBook_obj,"bookStoreAds":bookStore_obj})

def seller_homePage(request):
    storeAd_obj = BookStoreAd.objects.filter(bookStoreSeller = BookstoreSeller.objects.get(email = request.session.get("email")))
    return render(request,"seller/home_page.html",{"storeAds":storeAd_obj})

# book Show
def bookShow(request,user_id):
    user_ad = BookAd.objects.get(id=user_id)
    # print(user_ad.book_name)
    # print(user_id)
    return render(request,"post/book_show.html",{"user_ad":user_ad})
# book Show
def bookStoreShow(request,bookStore_id):
    seller_ad = BookStoreAd.objects.get(id=bookStore_id)
    # print(user_ad.book_name)
    # print(user_id)
    return render(request,"post/bookStore_show.html",{"seller_ad":seller_ad})

# Chat Box
def chatBox(request):
    return render(request,"post/chat_app.html")

# logout
def logOut(request):
    del request.session["email"]
    del request.session["islogin"]
    return redirect("home")

# profile Page
def profilePage(request):
    user = Users.objects.get(email = request.session.get("email"))
    try:
        UserImage.objects.get(user = Users.objects.get(email = request.session.get('email')))
    except Exception as err:
        return render(request,"accounts/profile.html",{"user_detail":user})
    else:
        img_obj = UserImage.objects.get(user = Users.objects.get(email = request.session.get('email')))
        return render(request,"accounts/profile.html",{"user_detail":user,"img_obj":img_obj})

# MyAds Page
def myAds(request):
    user_ads = BookAd.objects.filter(seller = Users.objects.get(email = request.session.get("email")))
    return render(request,"accounts/myads.html",{"user_ads":user_ads})

# seller Chatbox
# def seller_chatBox(request):
#     return render(request,"post/chat_app.html")
# seller Ad
def seller_Ad(request):
    return render(request,"seller/seller_post.html")
# after bookstore Ad post
def afterAdPost(request):
    if request.method == "POST":
        bookStore_detail = {
            "bookStoreSeller": BookstoreSeller.objects.get(email = request.session.get("email")),
            "bookStore_name": request.POST.get("bookStore_name"),
            "topic_book": request.POST.get("topic_book"),
            "description": request.POST.get("book_desc"),
            "image_1": request.POST.get("image_1"),
            "state": request.POST.get("state"),
            "city": request.POST.get("city"),
            "area": request.POST.get("area")
        }
        print(bookStore_detail)
        BookStoreAd.objects.create(**bookStore_detail)
        return redirect("seller_homePage")
# Seller profile
def sellerProfile(request,seller_id):
    book_seller = BookAd.objects.get(id = seller_id)
    book_seller_ads = BookAd.objects.filter(seller = book_seller.seller)
    seller_detail = Users.objects.get(email = book_seller.seller.email)
    print(book_seller_ads)
    return render(request,"accounts/seller_profile.html",{'seller_detail':seller_detail,'seller_ads':book_seller_ads})
# BookStoreSeller profile
def bookStoreSellerProfile(request,seller_email):
    bookStore_seller = BookstoreSeller.objects.get(email = seller_email)
    bookStore_seller_ads = BookStoreAd.objects.filter(bookStoreSeller = BookstoreSeller.objects.get(email = seller_email))
    # seller_detail = Users.objects.get(email = book_seller.seller.email)
    print(bookStore_seller.store_name)
    print("********")
    print(bookStore_seller_ads)
    return render(request,"accounts/storeSeller_profile.html",{'seller_detail':bookStore_seller,'seller_ads':bookStore_seller_ads})

# search Query
def searchQuery(request):
    location_query = request.GET["location"]
    book_query = request.GET["book_name"]
    book_ad_area = BookAd.objects.filter(area__icontains = location_query)
    book_ad_name = BookAd.objects.filter(book_name__icontains = book_query)
    ebook_ad = EBook.objects.filter(eBook_name__icontains = book_query)
    for i in ebook_ad:
        i.eBook_name = i.eBook_name.split(":")[0]
    book_ad = book_ad_area.union(book_ad_name)
    store_ad = BookStoreAd.objects.filter(area__icontains = location_query)
    if location_query == "none":
        msg = f"{book_query} doesn't match in databases. please Try Other Query.. "
    else:
        msg = f" No BookStore available in {location_query} location. please Try Another location.. "
    # if (len(store_ad) < 1 and len(book_ad) < 1 and len(ebook_ad) < 1):
    #     # params = {"bookStoreAds":store_ad, "bookAds":book_ad,"eBooks":ebook_ad,"query":msg}
    #     params = {"query":msg}
    #     return render(request,"post/search.html",params)
    # else:
    if book_query or location_query:
        params = {"bookStoreAds":store_ad, "bookAds":book_ad_area}
        return render(request,"post/search.html",params)
    elif book_query:
        params = {"bookStoreAds":store_ad, "bookAds":book_ad,"eBooks":ebook_ad}
        return render(request,"post/search.html",params)
    else:
        params = {"query":msg}
        return render(request,"post/search.html",params)
    
# search through lower header
def search(request,search_value):
    ebook_ad = EBook.objects.filter(eBook_description__icontains = search_value)
    bookStore_ad = BookStoreAd.objects.filter(topic_book__icontains = search_value)
    book_ad = BookAd.objects.filter(description__icontains = search_value)
    msg = f"{search_value} is not available."
    if (len(bookStore_ad) < 1 and len(book_ad) < 1 and len(ebook_ad) < 1):
        return render(request,"post/search.html",{"query":msg})
    else:
        params = {"bookStoreAds":bookStore_ad, "bookAds":book_ad,"eBooks":ebook_ad}
        return render(request,"post/search.html",params)

# search through lower header
def search_all(request,search_value):
    if search_value == "book":
        book_ad = BookAd.objects.all()
        params = {"bookAds":book_ad}
        return render(request,"post/search.html",params)
    else:
        bookStore_ad = BookStoreAd.objects.all()
        params = {"bookStoreAds":bookStore_ad}
        return render(request,"post/search.html",params)
    
# Chat
def chat(request):
    actual_sender = Users.objects.get(email = request.session.get("email"))
    print(actual_sender)
    # try:
    #     MessageByChat.objects.get(receiver = actual_sender)
    # except Exception as err:
    #     return HttpResponse("No Chat")
    # # receivers = []
    # else:
    re_obj = MessageByChat.objects.filter(receiver = actual_sender)
    actual_receiver = Users.objects.get(email = re_obj[0].sender.email)
    print(actual_receiver)

    print(MessageByChat.objects.filter(sender=actual_sender, receiver_id=actual_receiver) | MessageByChat.objects.filter(sender=actual_receiver, receiver_id=actual_sender))

    params = {"seller_detail":actual_receiver,"sender":actual_sender,"messages":MessageByChat.objects.filter(sender=actual_sender, receiver=actual_receiver) | MessageByChat.objects.filter(sender=actual_receiver, receiver=actual_sender)}
    return render(request,"post/chat_app_2.html",params)

# message show
def message_show(request):
    actual_sender = Users.objects.get(email = request.session.get("email"))
    print(actual_sender)
    re_obj = MessageByChat.objects.filter(receiver = actual_sender)
    actual_receiver = BookAd.objects.filter(seller = re_obj[0].sender)
    print(actual_receiver)

    print(MessageByChat.objects.filter(sender=actual_sender, receiver_id=actual_receiver[0].seller) | MessageByChat.objects.filter(sender=actual_receiver[0].seller, receiver_id=actual_sender))

    params = {"seller_detail":actual_receiver[0],"sender_detail":actual_sender,"messages":MessageByChat.objects.filter(sender=actual_sender, receiver=actual_receiver[0].seller) | MessageByChat.objects.filter(sender=actual_receiver[0].seller, receiver=actual_sender)}

    return render(request,"post/chat_app.html",params)

# message save
def message_save(request):
    actual_sender = Users.objects.get(email = request.session.get("email"))
    re_obj = MessageByChat.objects.filter(receiver = actual_sender)
    # receivers = []
    actual_receiver = Users.objects.get(email = re_obj[0].sender.email)
    if request.method == 'POST':
        msg = {
            "sender" : actual_sender,
            "receiver" : actual_receiver,
            "message" : request.POST.get("message")
        }
        MessageByChat.objects.create(**msg)
    return redirect("chat")

# store Chat box
def storeChatBox(request,seller_id):
    receiver = BookStoreAd.objects.get(id = seller_id)
    sender = Users.objects.get(email = request.session.get("email"))
    return render(request,"post/chat_app.html",{"seller_detail": receiver,"sender_detail": sender})
    # return render(request,"post/chat_app.html",{"seller_detail": receiver,"sender_detail": sender,'messages': MessageByChat.objects.filter(sender=sender, receiver=receiver.bookStoreSeller) | MessageByChat.objects.filter(sender=receiver.bookStoreSeller, receiver=sender)})
    # return  render(request,"post/chat_app.html")


# upload Image
def uploadImg(request):
    if request.method == 'POST':
        l_img = request.POST.get('p_img')
        data = {
            'image' : l_img,
            'user' : Users.objects.get(email = request.session.get('email'))
        }
        # Image.objects.create(**data)
        try:
            UserImage.objects.get(user = Users.objects.get(email = request.session.get('email')))
        except Exception as error:
            UserImage.objects.create(**data)
            # img_obj = UserImage.objects.get(author = Users.objects.get(email = request.session.get('email')))    
            # user = Users.objects.get(email = request.session.get("email"))
            # return render(request,"accounts/profile.html",{"user_detail":user,"img_obj":img_obj})
            return redirect("profile")
        else:
            img_obj = UserImage.objects.get(user = Users.objects.get(email = request.session.get('email')))
            img_obj.image = l_img
            img_obj.save()
            return redirect("profile")
            # user = Users.objects.get(email = request.session.get("email"))
            # return render(request,"accounts/profile.html",{"user_detail":user,"img_obj":img_obj})
        return HttpResponse("hi")

# change Profile Detail
def changeDetail(request):
    if request.method == 'POST':
        full_name = request.POST.get("fullname")
        email = request.POST.get("email")
        phone_no = request.POST.get("phonenumber")
        user_obj = Users.objects.get(email = request.session.get("email"))
        user_obj.full_name = full_name
        user_obj.email = email
        user_obj.phone_no = phone_no
        user_obj.save()
        return redirect("profile")


# Forgot password 
def forgot_password(request):
    return render(request,"accounts/forgot_password.html")

# Get OTP Number for Change password and Enter the email
def after_email(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        try:
            Users.objects.get(email = email)
        except Exception as err:
            msg = "Please Enter the valid Email..."
            return render(request,"accounts/forgot_password.html",{"email_msg": msg})
        else:
            otp = randint(1000,9999)
            subject = "OTP for change password"
            msg = f"""Welcome To Booksporium
            Here is Your OTP to change your password OTP is {otp}"""
            to_mail = "web.mihir017@gmail.com"
            try:
                send_mail(subject, msg, settings.EMAIL_HOST_USER, [to_mail], auth_password = settings.EMAIL_HOST_PASSWORD)
            except Exception as err:
                msg = "SERVER DOWN"
                print(err)
                return redirect("signin")
            else:
                request.session['email'] = email
                request.session['otp'] = otp
                return render(request,"accounts/otp.html")

# Enter The OTP Trough mail
def after_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get("otp_no")
        actual_otp = str(request.session['otp'])
        if user_otp == actual_otp:
            return render(request,"accounts/change_password.html")
        else:
            msg = "OTP does not match !!"
            del request.session['email']
            del request.session['otp']
            return render(request,"accounts/otp.html",{"otp_msg" : msg})

# Enter the new Password and Save()
def afterchangePassword(request):
    if request.method == "POST":
        if len(request.POST.get("new_password")) > 7:
            u_letter,l_letter,n_letter,s_char = 0,0,0,0
            for letter in (request.POST.get("new_password")):
                if letter.isupper():
                    u_letter += 1  
                elif letter.islower():
                    l_letter += 1  
                elif letter.isnumeric():
                    n_letter += 1
                elif letter in "<>?@#$%&*()!":
                    s_char += 1
            if (u_letter > 0) and (l_letter > 0) and (n_letter > 0) and (s_char > 0):
                new_password = request.POST.get("new_password")
                new_repeat_password = request.POST.get("repeat_password")
                actual_email = request.session['email']
                if new_password == new_repeat_password:
                    user_obj = Users.objects.get(email = actual_email)
                    user_obj.password = new_password
                    user_obj.save()
                    return redirect("signin") 
                else:
                    msg = "Password Does't Match..."
                    return render(request,"accounts/change_password.html",{"repeat_password_msg": msg})
            else:
                msg = "Password Contain one upper, lower, numeric and special character.."
                return render(request,"accounts/change_password.html",{"password_msg": msg})
        else:
                msg = "Password Contain Minimum 8 character.."
                return render(request,"accounts/change_password.html",{"password_msg": msg})  