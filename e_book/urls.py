from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.eBook_detail, name = "eBook"),
    path("buy_now/",views.buyNow, name = "buyNow"),
    path("handlerequest/",views.handlerequest, name = "HandleRequest")
]