from django.conf  import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    query = models.CharField(max_length=200)
    message= models.TextField()


    def __str__(self):
        return self.query

    def get_absolute_url(self):
        return reverse('thankyou', args=[str(self.id)])

class Manager(models.Model):
    name               = models.CharField(max_length=200)
    author             = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    price              = models.IntegerField()
    description        = models.CharField(max_length=200)
    product_photo      = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager_edit', args=[str(self.id)])



