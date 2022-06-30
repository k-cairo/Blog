from django.forms import ModelForm
from Blog.models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'chakras', 'image', 'content']
