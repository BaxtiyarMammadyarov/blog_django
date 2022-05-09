from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    content = {'posts': posts}
    return render(request, 'post/index.html', content)


def post_detail(request, post_id):
    print(post_id)
    post = get_object_or_404(Post, id=int(post_id))
    content = {'post': post}
    return render(request, 'post/detail.html', content)


def post_create(request):
    return HttpResponse('<b>create page </b>')


def post_update(request):
    return HttpResponse('<b>update page </b>')


def post_delete(request):
    return HttpResponse('<b>delete page </b>')
