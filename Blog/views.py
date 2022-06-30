from django.shortcuts import render
from BlogWebsite.form import BlogPostForm
from .models import BlogPost
from datetime import date


def index(request):
    all_posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', context={"all_posts": all_posts})


def post(request, slug):
    target_post = BlogPost.objects.filter(slug=slug).get()
    print(target_post)
    return render(request, 'blog/post.html', context={'target_post': target_post})


def edit_post(request, slug):
    target_post = BlogPost.objects.filter(slug=slug).get()
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.slug = blog_post.title
            blog_post.published_date = date.today()
            blog_post.author = 'CAIRO Kévin'
            blog_post.save()
            return render(request, 'blog/index.html')
    else:
        form = BlogPostForm(initial={'title': target_post.title,
                                     'chakras': target_post.chakras,
                                     'image': target_post.image,
                                     'content': target_post.content})
    return render(request, 'blog/edit-post.html', context={'form': form,
                                                           'target_post': target_post})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.slug = blog_post.title
            blog_post.published_date = date.today()
            blog_post.author = 'CAIRO Kévin'
            blog_post.save()
            return render(request, 'blog/index.html')
    else:
        form = BlogPostForm()

    return render(request, 'blog/new-post.html', context={'form': form})
