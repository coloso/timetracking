from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
