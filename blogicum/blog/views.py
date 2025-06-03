from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def index(request):
    posts = Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.select_related('category', 'location'),
        pk=pk,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = category.post_set.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('category', 'location').order_by('-pub_date')
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': posts}
    )
