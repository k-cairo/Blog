from django.db import models
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titre')
    author = models.CharField(max_length=100)
    slug = models.SlugField()
    published_date = models.DateField()
    chakras = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True, verbose_name="Contenu")
    image = models.URLField(blank=True)

    def __str__(self):
        return self.title
