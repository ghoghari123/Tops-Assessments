from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# BLOG LIST + FILTER
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')

    author = request.GET.get('author')
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if author:
        blogs = blogs.filter(author__username__icontains=author)

    if category:
        blogs = blogs.filter(category__id=category)

    if start_date and end_date:
        blogs = blogs.filter(created_at__range=[start_date, end_date])

    categories = Category.objects.all()

    return render(request, 'blog_list.html', {
        'blogs': blogs,
        'categories': categories
    })


# CREATE BLOG
@login_required
def create_blog(request):
    form = BlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        form.save_m2m()
        return redirect('blog_list')

    return render(request, 'blog_form.html', {'form': form})


# UPDATE BLOG
@login_required
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author != request.user:
        return redirect('blog_list')

    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('blog_list')

    return render(request, 'blog_form.html', {'form': form})


# DELETE BLOG
@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author == request.user:
        blog.delete()

    return redirect('blog_list')


# BLOG DETAIL
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})