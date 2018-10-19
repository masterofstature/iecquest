from django.db import models
from django.conf import settings


class Quest(models.Model):
    start_time = models.DateTimeField('start_time', auto_now=False)
    end_time = models.DateTimeField('end_time')
    slug = models.SlugField()
    title = models.CharField(max_length=50)

class ModelVisual(models.Model):
    model = models.FileField(upload_to='media', null=True, blank=True)
    url = models.URLField(max_length=500)
    slug = models.SlugField()
    scales=models.CharField(max_length=50, default='1 1 1')
    rotation=models.CharField(max_length=50, default='0 0 0')
    position=models.CharField(max_length=50, default='0 0 0')
    quest = models.ForeignKey(Quest, verbose_name="quest", on_delete=models.CASCADE)