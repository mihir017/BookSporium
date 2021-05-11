from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Users)
admin.site.register(BookstoreSeller)
admin.site.register(BookStoreAd)
admin.site.register(MessageByChat)
admin.site.register(UserImage)