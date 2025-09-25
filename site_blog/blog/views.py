from django.shortcuts import render, get_object_or_404
from .models import Post

#request - всегда
def post_list(request):
    posts = Post.objects.all() #все записи из БД
    return render(request, 'blog/post_list.html',
                  {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,
                  'blog/post_detail.html',
                  {'post': post})

# Create your views here.
