from django.http import HttpResponseRedirect
from django.shortcuts import render
from BlogWebsite.form import BlogPost


def index(request):
    return render(request, 'blog/index.html')


def new_post(request):
    if request.method == "POST":
        form = BlogPost(request.POST)
        if form.is_valid():
            pass
            return HttpResponseRedirect('/thanks/')

    else:
        form = BlogPost()

    return render(request, 'blog/make-post-2.html', context={'form': form})
