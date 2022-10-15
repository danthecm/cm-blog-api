from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.


class DateAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogTag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(DateAbstract):
    tags = models.ManyToManyField(BlogTag, related_name="blogs")
    title = models.CharField(max_length=225, unique=True)
    author = models.ForeignKey(
        User, related_name="created_blogs", on_delete=models.CASCADE)
    content = HTMLField()
    slug = models.SlugField(default="", editable=False, max_length=225)
    cover = models.ImageField(upload_to="blog_api/", default="blog_api/default.jpg")
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.author.username}"
    


class BlogComment(DateAbstract):
    blog = models.ForeignKey(
        Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="Anonymous")
    ip = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.blog.title} - {self.name}"
    

