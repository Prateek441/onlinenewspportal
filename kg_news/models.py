from django.db import models
from datetime import datetime
from django.db.models.signals import post_save

class City(models.Model):
    city = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

class State(models.Model):
    STATE_CHOICE = (
        ('Rajasthan', "Rajasthan"),
        ('Madhya Pradesh', "Madhya Pradesh"),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Maharastra', 'Maharastra'),
        ('Gujrat', 'Gujrat'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Bihar', 'Bihar')
    )
    state = models.CharField(choices=STATE_CHOICE, max_length=50, default='')
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.state

class SubCategory(models.Model):
    sub_cat = models.CharField(max_length=50)
    def __str__(self):
        return self.sub_cat

class Categories(models.Model):
    category = models.CharField(max_length=50, unique=True)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.category

class RelImg(models.Model):
    img1 = models.ImageField(upload_to='uploads/posts', default='pna.jpg')


class Add_news_ch(models.Model):
    chname = models.CharField(max_length=50)
    chimg = models.ImageField(upload_to='uploads/chimg', default='noimg.jpg')
    cdate = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    reg_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.chname

class ChPost(models.Model):
    ch_post = models.ForeignKey(Add_news_ch, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    Description = models.TextField()
    img = models.ImageField(upload_to='uploads/posts', default='pna.jpg')
    related_img = models.ForeignKey(RelImg, on_delete=models.CASCADE)
    cdate = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ChannelDetails(models.Model):
    ch_detail = models.OneToOneField(Add_news_ch, on_delete=models.CASCADE)
    chimg = models.ImageField(upload_to='uploads/chcover', default='ch_cover.jpg')
    owner_name = models.CharField(max_length=50)
    Ch_desc = models.TextField()
    since = models.DateField(default=datetime.today)
    LANG_CHOICE = (
        ('h', "Hindi"),
        ('e', "English"),
        ('m', 'marathi'),
        ('g', 'gujrati'),
        ('t', 'tamil'),
        ('p', 'punjabi')
    )
    language =models.CharField(choices=LANG_CHOICE, max_length=15, default='')

class Query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    query = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Slider(models.Model):
    slider = models.ImageField(upload_to='uploads/slider')
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


class WelMsg(models.Model):
    msg1 = models.TextField()
    msg2 = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

class Media(models.Model):
    img = models.ImageField(upload_to='stationary', default='none.jpg')
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


def make_cprofile(sender,instance,created,**kwargs):
    if created:
        ChannelDetails.objects.create(ch_detail=instance)

post_save.connect(make_cprofile,sender=Add_news_ch)