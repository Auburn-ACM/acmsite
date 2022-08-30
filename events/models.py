from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name