from django.db import models
from accounts.models import Users
# Create your models here.

# e-book Model
LANGUAGE_CHOICE = (
    ("english","english"),
    ("hindi","hindi"),
    ("gujrati","gujrati"),
    )

class EBook(models.Model):
    eBook_name = models.CharField(max_length=100)
    eBook_author = models.CharField(max_length=100)
    eBook_price = models.FloatField()
    eBook_description = models.TextField()
    eBook_image = models.ImageField(upload_to = "static/images")
    eBook_file = models.FileField(upload_to='staitc/file')
    eBook_publisher = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    language = models.CharField(choices = LANGUAGE_CHOICE, max_length=50)
    file_size = models.CharField(max_length = 100)
    print_length = models.CharField(max_length = 100)

    def __str__(self):
        return self.eBook_name

