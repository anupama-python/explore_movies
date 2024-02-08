from django.db import models

# Create your models here.
class Malayalam(models.Model):
    name=models.CharField(max_length=250)
    director=models.CharField(max_length=250)
    year=models.DateField()
    image=models.ImageField(upload_to='img/%y',default="")
    def __str__(self):
        return self.name

class English(models.Model):
    e_name=models.CharField(max_length=250)
    e_director = models.CharField(max_length=250)
    e_year = models.DateField()
    e_image = models.ImageField(upload_to='imgs/%y', default="")

    def __str__(self):
        return self.e_name
class Hindi(models.Model):
    h_name=models.CharField(max_length=250)
    h_director = models.CharField(max_length=250)
    h_year = models.DateField()
    h_image = models.ImageField(upload_to='imgs/%y', default="")

    def __str__(self):
        return self.h_name
