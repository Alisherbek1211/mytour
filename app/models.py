from django.db import models

class User(models.Model):
    
    GENDER_STATUS = (
        ('Male','Male'),
        ('Female','Female'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    parol = models.CharField(max_length=255)
    manzil = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    gender = models.CharField(max_length=6,choices=GENDER_STATUS,default='Male')
    birth_date = models.DateTimeField(null=True,blank=True)
    viza = models.FileField(null=True,blank=True)
    passport = models.FileField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)