from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    date_time_created = models.DateTimeField(auto_now_add=True)  # Background field
    date_time_updated = models.DateTimeField(auto_now=True)  # Background field
    delete_tweet = models.BooleanField(default=False)

    def short_text(self):
        short_text = self.text[:10] + '...'
        return short_text

    def __str__(self):
        return self.short_text()
    
    