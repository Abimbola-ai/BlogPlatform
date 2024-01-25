from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self) -> str:
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    
class BlogPosts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    summary = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPosts, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class BlogPostCategory(models.Model):
    blog_post = models.ForeignKey(BlogPosts, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

