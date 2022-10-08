from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user_pdf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='user_images')
    user_pdf = models.FileField(upload_to='user_pdfs')
