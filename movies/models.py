from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class MovieData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating  = models.FloatField()
    typ = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to='Images/', default="Images/None/NoImg.jpg")