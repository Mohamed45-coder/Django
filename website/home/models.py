from django.db import models

# Create your models here.

class data(models.Model):
    location=models.CharField(max_length=100)
    hotel=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='pics')
    