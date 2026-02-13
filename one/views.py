# django o'zin kutubxonlar
from gc import get_objects

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# bizni applarmiz fayilar chaqirish
from .models import Post

class PostListViews(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/main.html'


def post_datail(request, year, month,day,slug):
    post = get_object_or_404(Post,slug=slug,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {
        'post':post
    }
    return render(request, 'blog/post/data.html',context)