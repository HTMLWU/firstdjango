from django.db import models
from six import python_2_unicode_compatible
# Create your models here.

# python_2_unicode_compatible 装饰器用于兼容 Python2


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateField(auto_now_add=True)

    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
