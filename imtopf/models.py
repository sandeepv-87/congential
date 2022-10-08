from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user_pdf(models.Model):
    image_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    user_image = models.ImageField(upload_to='user_images')
    user_pdf = models.FileField(upload_to='user_pdfs',default=None)



class testing(models.Model):
    img = models.ImageField(upload_to='imgs')