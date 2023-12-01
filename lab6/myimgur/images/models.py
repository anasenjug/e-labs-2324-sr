from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=512)
    url = models.CharField(max_length=512)
    created_at = models.DateTimeField()
    


