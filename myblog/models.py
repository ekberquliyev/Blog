from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class NavbarModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    title_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'


class Footer(models.Model):
    logo_image = models.ImageField(upload_to = 'blog_logo', null = True, blank = True)
    logo_url = models.URLField(null=True, blank=True)

class Settings(models.Model):
    background_image = models.ImageField(upload_to='blog_images', null=True, blank=True )
    blog_title = models.CharField(max_length=50, null=True, blank=True)
    blog_subtitle = models.CharField(max_length=80, null=True, blank=True)
    logo = models.ImageField(upload_to = 'blog_logo', null = True, blank = True)


class PostModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100, null=True, blank=True)
    post_subtitle = models.CharField(max_length=254, null=True, blank=True)
    post_date = models.DateField(auto_now=True)
    post_text = models.TextField(null=True, blank=True)
    post_head_image = models.ImageField(upload_to = 'post_image', null=True, blank=True)

    def __str__(self):
        return f'{self.post_title} / {self.post_date}'

class PostImageModel(models.Model):
    post_id = models.ForeignKey('PostModel', on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'post_image', null=True, blank=True)

class AboutModel(models.Model):
    text = models.CharField(max_length=299, null=True, blank=True)
    text_date = models.DateField(auto_now=True)

class PostContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    text = models.TextField()