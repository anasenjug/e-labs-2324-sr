from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=256, blank=False)
    title = models.CharField(max_length=128, blank=False)
    pub_date = models.DateTimeField('Published at')
    def __str__(self):
        return f"{self.id}-{self.title[:20]}"
    
    def liked_by(self, user):
        try:
            return self.like_set.filter(user=user).count() > 0
        except:
            return False
    
    def toggle_like(self,user):
        if self.liked_by(user):
            like = self.like_set.filter(user=user).first()
            like.delete()
            return False
        else:
            like= self.like_set.create(user=user)
            return True
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField('Published at')
    approved = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.id}-{self.image.title[:15]}-{self.text}"
    
class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ForeignKey(Image, on_delete=models.CASCADE)