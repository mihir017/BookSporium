from django.urls import path, include
from . import views

urlpatterns = [
    # path("",views.afterSignin, name = "afterSignin"),
    # path("",views.homePage, name = "home_page"),
    # path("index/",views.homePage,name = "home_page"),
    path("",views.postBookAD, name = "post_book_ad"),
    path("afterPost/",views.submitPost, name = "afterPost")
]