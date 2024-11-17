from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    