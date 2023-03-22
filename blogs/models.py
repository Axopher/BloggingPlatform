from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    # body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title+' | '+str(self.author)

    def get_absolute_url(self):
        # return reverse('detail-article',args=[str(self.id)])
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    # recipient = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return '%s - %s ' % (self.post.title,self.name)

    class Meta:
        ordering = ['-created']