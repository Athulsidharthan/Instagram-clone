from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    image=models.ImageField(upload_to='Post')
    caption=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to='Profile_img')
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    dateofbirth = models.DateField()
    GENDER_OPTIONS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_OPTIONS)

    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    post= models.ForeignKey(Post, on_delete=models.CASCADE, null=True)