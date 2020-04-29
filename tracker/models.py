from django.db import models
from datetime import datetime   
# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=100)
    mail=models.EmailField()
    message= models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name