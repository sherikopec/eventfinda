from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    venue = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category', related_name='events')



class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

