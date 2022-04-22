from django.db import models

class User(models.Model):

    # First and last name might not be unique
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    # email must be unique
    email = models.CharField(max_length=128, unique=True)


