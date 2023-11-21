from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.CharField(max_length=20, primary_key = True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    profession1 = models.CharField(max_length=100)
    profession2= models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name