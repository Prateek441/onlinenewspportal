from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Admin(models.Model):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    reg_id = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Adminprofile(models.Model):
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image =models.ImageField(upload_to='profile', default='abcd.jpg')
    about =models.TextField()
    gender =models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    cover =models.ImageField(upload_to='cover', default='cover.jpg')
    address = models.TextField()
    def __str__(self):
        return self.admin.email


def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Adminprofile.objects.create(admin =instance)
post_save.connect(create_user_profile, sender =Admin)