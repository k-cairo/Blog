from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published_date = models.DateField()
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
