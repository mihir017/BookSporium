from django.urls import path, include
from . import views

urlpatterns = [
    # path("",views.afterSignin, name = "afterSignin"),
    # path("",views.homePage, name = "home_page"),
    # path("index/",views.homePage,name = "home_page"),
    path("",views.sellerChatBox,name="sellerChatBox"),
    path("message_list/",views.message_list, name = "message_list")
    # path("/message_list/<str:recevier_id>/",views.message_list, name = "message_list")
    # path("afterPost/",views.submitPost, name = "afterPost")
]