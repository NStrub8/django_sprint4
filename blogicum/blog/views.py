from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def index(request):
    posts = Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'page_obj': page_obj})


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

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'page_obj': page_obj
        }
    )


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.select_related('category').filter(
        author=user
    ).order_by('-pub_date')

    if request.user != user:
        posts = posts.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/profile.html',
        {
            'profile_user': user,
            'page_obj': page_obj
        }
    )
