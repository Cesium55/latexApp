from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    password = models.CharField(max_length=100, verbose_name="Password")

    def __str__(self):
        return self.name

