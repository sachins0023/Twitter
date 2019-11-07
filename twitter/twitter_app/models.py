from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(_(""), max_length=254)
    name = models.CharField(_(""), max_length=50)
    
    def __str__(self):
        return self.name
    
class Tweet(models.Model):
    text = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date)
    time = models.TimeField(default=date)
    
    