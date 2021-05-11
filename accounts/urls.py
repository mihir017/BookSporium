from django.urls import path, include
from . import views

urlpatterns = [
    # first url
    path("",views.home, name = "home"),
    
    # sign in, sign up
    path("signin/",views.signin, name = "signin"),
    path("signup/",views.signup, name = "signup"),
    path("store_signup/",views.storeSignup, name = "storeSignup"),
    
    # after signin, after signup
    path("aftersignup/",views.afterSignup),
    path("afterBookStoresignup/",views.afterBookStoreSignup, name = "afterBookStoreSignup"),
    path("home/",views.afterSignin, name = "afterSignin"),
    path("home/",views.afterSignin, name = "afterSignin"),
    # path("bookStoreHome/",views.afterBookStoreSignin, name = "afterBookStoreSignin"),

    # main pages bot user and seller
    path("home_page/",views.homePage, name = "homePage"),   
    path("seller_home_page/",views.seller_homePage, name = "seller_homePage"),
    
    # main pages both user and seller
    path("home/search_query/",views.searchQuery, name = "searchQuery"),
    path("home_page/search_query/",views.searchQuery, name = "searchQuery"),
    # search main pages bot user and seller
    # path("home/search_query/",views.searchQuery, name = "searchQuery"),
    path("home_page/search/<str:search_value>",views.search, name = "search"),
    path("home_page/search_all/<str:search_value>",views.search_all, name = "search_all"),
    
    # book Show
    path("home/book_show/<str:user_id>",views.bookShow, name = "bookShow"),
    path("home_page/book_show/<str:user_id>",views.bookShow, name = "bookShow"),
    
    # seller profile Show
    path("home/book_show/seller_profile/<str:seller_id>",views.sellerProfile, name = "sellerProfile"),
    path("home_page/book_show/seller_profile/<str:seller_id>",views.sellerProfile, name = "sellerProfile"),
    
    # bookStore seller profile Show
    path("home/bookStore_show/bookStoreSeller_profile/<str:seller_email>",views.bookStoreSellerProfile, name = "bookStoreSellerProfile"),
    path("home_page/bookStore_show/bookStoreSeller_profile/<str:seller_email>",views.bookStoreSellerProfile, name = "bookStoreSellerProfile"),
    
    # bookStore Show
    path("home/bookStore_show/<str:bookStore_id>",views.bookStoreShow, name = "bookStoreShow"),
    path("home_page/bookStore_show/<str:bookStore_id>",views.bookStoreShow, name = "bookStoreShow"),
    
    # book store chat 
    path("home/bookStore_show/chat_box/<str:seller_id>",views.storeChatBox, name = "storeChatBox"),
    path("home_page/bookStore_show/chat_box/<str:seller_id>",views.storeChatBox, name = "storeChatBox"),
    
    # chat
    path("home/chat/",views.chat, name = "chat"),
    path("home_page/chat/",views.chat, name = "chat"),
    
    # upload Image and change Detail
    path("home_page/upload_img/",views.uploadImg, name = "uploadImg"),
    path("home_page/change_detail/",views.changeDetail, name = "changeDetail"),
    
    # message Show
    path("home/chat/message_save/",views.message_save, name = "message_save"),
    path("home_page/chat/message_save/",views.message_save, name = "message_save"),

    # Chat box
    # path("home/book_show/chat_box/",views.chatBox, name = "chatBox"),
    # path("home_page/book_show/chat_box/",views.chatBox, name = "chatBox"),
    path("home_page/book_show/chat_box/<str:reciever_id>/",include("users.urls")),
    path("home/book_show/chat_box/<str:reciever_id>/",include("users.urls")),
    # chat2
    path("home_page/book_show/chat/",views.message_show,name="message_show"),
    path("home/book_show/chat/",views.message_show,name="message_show"),
 
    # path("home_page/book_show/chat_box/message_list/",include("users.urls"), name = "message_list"),
    # path("home/book_show/chat_box/message_list/",include("users.urls"), name = "message_list"),
    
    # Post Book AD
    path("home/post_book_ad/",include("posts.urls")),
    path("home_page/post_book_ad/",include("posts.urls")),
    # path("home/",include("posts.urls")),
    
    # e-Book AD
    path("home/e-book/<str:e_book_id>/",include("e_book.urls")),
    path("home_page/e-book/<str:e_book_id>/",include("e_book.urls")),

    # Profile 
    path("home/profile/",views.profilePage, name= "profile"),
    path("home_page/profile/",views.profilePage, name= "profile"),
   
    # MyAds 
    path("home/myads/",views.myAds, name= "myads"),
    path("home_page/myads/",views.myAds, name= "myads"),

    # logout 
    path("home/logout/",views.logOut, name= "logOut"),
    path("home_page/logout/",views.logOut, name= "logOut"),

    # forgot Password
    path("signin/forgot_password/",views.forgot_password),
    path("home/forgot_password/",views.forgot_password),
    path("home/forgot_password/after_email/",views.after_email),
    path("signin/forgot_password/after_email/",views.after_email),
    path("signin/forgot_password/after_email/after_otp/",views.after_otp),
    path("home/forgot_password/after_email/after_otp/",views.after_otp),
    path("home/forgot_password/after_email/after_otp/afterchangePassword/",views.afterchangePassword),
    path("signin/forgot_password/after_email/after_otp/afterchangePassword/",views.afterchangePassword),


    #  seller account.................
    # seller chatbox
    # path("seller_home_page/seller_chatBox/",views.seller_chatBox, name = "seller_chatBox"),
    # path("home/seller_chatBox/",views.seller_chatBox, name = "seller_chatBox"),
    path("seller_home_page/seller_chatBox/<str:reciever_id>/",include("users.urls"), name = "seller_chatBox"),
    path("home/seller_chatBox/<str:reciever_id>/",include("users.urls"), name = "seller_chatBox"),
    # seller Ads
    path("seller_home_page/seller_ad/",views.seller_Ad, name = "seller_Ad"),
    path("home/seller_ad/",views.seller_Ad, name = "seller_Ad"),
    # After Ad post
    path("seller_home_page/seller_ad/afterAdPost/",views.afterAdPost, name = "afterAdPost"),
    path("home/seller_ad/afterAdPost/",views.afterAdPost, name = "afterAdPost")

]