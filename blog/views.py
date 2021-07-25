from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get("page")

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request, "blog/post/list.html", {"page": page, "posts": data})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/post/detail.html", {"post": post})
