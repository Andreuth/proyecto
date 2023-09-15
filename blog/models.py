from django.db import models
import datetime

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TimeField()
    image=models.ImageField(upload_to='blog/images')
    date=models.DateField(datetime.date.today)
# Create your models here.
