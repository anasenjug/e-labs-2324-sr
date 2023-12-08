from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=512)
    pub_date = models.DateTimeField()
    url = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.id} - {self.title}"
    
class Comment(models.Model):
    text= models.CharField(max_length=512)
    created_at=models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image.id}:{self.text[:25]}"
    
