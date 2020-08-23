from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    website=models.URLField(blank=True,null=True)
    def __str__(self):
        return self.user.username



class Actor(models.Model):
    name=models.CharField(max_length=256)
    movie=models.CharField(max_length=256)
    age=models.PositiveIntegerField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    about=models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app12345:detail',kwargs={'pk':self.pk})