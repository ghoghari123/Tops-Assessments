from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import BlogForm
from interactions.models import Like, Comment
from interactions.forms import CommentForm


def blog_list(request):
    blogs = Post.objects.all().order_by('-created_at')

    author = request.GET.get('author')
    category = request.GET.get('category')

    if author:
        blogs = blogs.filter(author__username__icontains=author)

    if category:
        blogs = blogs.filter(category__id=category)

    categories = Category.objects.all()

    return render(request, 'blog/blog_list.html', {
        'blogs': blogs,
        'categories': categories
    })

def blog_detail(request, id):
    blog = get_object_or_404(Post, id=id)

    comments = Comment.objects.filter(post=blog).order_by('-created_at')
    likes_count = Like.objects.filter(post=blog).count()

    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(user=request.user, post=blog).exists()

    form = CommentForm()

    return render(request, 'blog/blog_detail.html', {
        'blog': blog,
        'comments': comments,
        'likes_count': likes_count,
        'liked': liked,
        'form': form
    })

@login_required
def create_blog(request):
    form = BlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        form.save_m2m()
        return redirect('blog_list')

    return render(request, 'blog/blog_form.html', {'form': form})


@login_required
def update_blog(request, id):
    blog = get_object_or_404(Post, id=id)

    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('blog_list')

    return render(request, 'blog/blog_form.html', {'form': form})


@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Post, id=id)
    blog.delete()
    return redirect('blog_list')


# def blog_detail(request, id):
#     blog = get_object_or_404(Post, id=id)
#     return render(request, 'blog/blog_detail.html', {'blog': blog})