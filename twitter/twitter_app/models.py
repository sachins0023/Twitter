from django.db import models
import datetime
import pytz

# Create your models here.

class User(models.Model):
    email = models.EmailField(_(""), max_length=254, primary_key=True)
    name = models.CharField(_(""), max_length=50)
    
    def __str__(self):
        return self.name
    
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default = False)
    
    def edited(self):
        if (self.date_time_created-self.date_time_updated) > datetime.timedelta(seconds=1):
            return True
        else:
            return False
    
    def __str__(self):
        return self.text[:10]+'...'
    
    