from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

# Количество постов на главной.
number_of_posts = 5


def index(request):
    """Главная с постами."""
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True, category__is_published=True,
        pub_date__lte=timezone.now()
    )[:number_of_posts]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Пост."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=post_id, is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Посты по заданой категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug, is_published=True
    )
    post_list = Post.objects.filter(
        is_published=True,
        category=category,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
