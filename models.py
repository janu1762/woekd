from django.db import models

# Create your models here.
class Profile(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    dob = models.DateField(max_length=8)
    email = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=255)
    
    


