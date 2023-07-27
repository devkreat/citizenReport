from django.db import models

# Create your models here.
class Post(models.Model):
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    decription = models.CharField(max_length=500)

    def __str__(self):
        return self.address
