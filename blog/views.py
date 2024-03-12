from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {
        'posts': posts
    })

def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id, status=Post.Status.published)

    return render(request, 'blog/detail.html',{
        'post':post
    })