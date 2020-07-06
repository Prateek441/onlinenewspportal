from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Users(models.Model):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Userprofile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    image =models.ImageField(upload_to='profile', default='abcd.jpg')
    about =models.TextField()
    gender =models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    cover =models.ImageField(upload_to='cover', default='cover.jpg')
    address = models.TextField()
    def __str__(self):
        return self.user.email


def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Userprofile.objects.create(user =instance)
post_save.connect(create_user_profile, sender =Users)