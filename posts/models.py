from django.db import models
from accounts.models import *
# Create your models here.

# Book post
class BookAd(models.Model):
    seller = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_price = models.FloatField()
    description = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.seller.email


