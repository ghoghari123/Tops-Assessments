from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import Like, Comment
from .forms import CommentForm
from .models import Follow
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from blog.models import Post
from interactions.models import Follow

def profile_view(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)

    posts = Post.objects.filter(author=user_profile)
    followers = Follow.objects.filter(following=user_profile).count()
    following = Follow.objects.filter(follower=user_profile).count()

    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=user_profile
        ).exists()

    return render(request, 'users/profile.html', {
        'user_profile': user_profile,
        'posts': posts,
        'followers': followers,
        'following': following,
        'is_following': is_following
    })

@login_required
def toggle_follow(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if target_user != request.user:
        follow = Follow.objects.filter(follower=request.user, following=target_user)

        if follow.exists():
            follow.delete()
        else:
            Follow.objects.create(follower=request.user, following=target_user)

    return redirect('profile', user_id=target_user.id)


# LIKE / UNLIKE
@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like = Like.objects.filter(user=request.user, post=post)

    if like.exists():
        like.delete()
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect('blog_detail', id=post_id)


#  ADD COMMENT
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

    return redirect('blog_detail', id=post_id)


# DELETE COMMENT
@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if comment.user == request.user:
        comment.delete()

    return redirect('blog_detail', id=comment.post.id)

@login_required
def create_blog(request):
    if request.user.profile.role != 'author':
        return redirect('blog_list')