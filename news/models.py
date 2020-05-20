from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class NewsArticoliModel(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", default=1)

    def __str__(self):
        return self.titolo

class NewsGiornalistiModel(models.Model):
    user= models.CharField(max_length=100)
    
    

    
