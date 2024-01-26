from django.db import models

# Create your models here.

class UserStream(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
