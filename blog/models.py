from django.db import models
from datetime import datetime

from django.db.models.fields.files import ImageField


class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='uploads')
    datetime = models.DateTimeField(default=datetime.now())
    detail = models.CharField(max_length=150)

    def __str__(self):
        return self.title
