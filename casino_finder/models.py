from django.db import models

# Create your models here.

class Casino(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


