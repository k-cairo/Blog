from django import forms


class BlogPost(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=50)
    image = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea)

