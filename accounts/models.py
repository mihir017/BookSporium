from django.db import models

# Create your models here.

class Users(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key = True)
    password = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)

    def __str__(self):
        return self.email

class BookstoreSeller(models.Model):
    store_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key = True)
    password = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)
    
    def __str__(self):
        return self.email

# Book post
class BookStoreAd(models.Model):
    bookStoreSeller = models.ForeignKey(to=BookstoreSeller, on_delete=models.CASCADE)
    bookStore_name = models.CharField(max_length=100)
    topic_book = models.CharField(max_length=100)
    description = models.TextField()
    image_1 = models.ImageField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.bookStoreSeller.email

class MessageByChat(models.Model):
    sender = models.ForeignKey(to = Users, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(to = Users, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)

class UserImage(models.Model):
    user = models.ForeignKey(to = Users, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.user.email