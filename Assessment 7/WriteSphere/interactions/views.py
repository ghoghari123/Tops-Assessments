from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
from .models import *


# ❤️ LIKE / UNLIKE
@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()   # unlike

    return redirect('home')


# 💬 ADD COMMENT
@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )

    return redirect('post_detail', id=id)


# ✏️ EDIT COMMENT
@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    # only owner can edit
    if comment.user != request.user:
        return redirect('home')

    if request.method == 'POST':
        comment.text = request.POST.get('text')
        comment.save()
        return redirect('post_detail', id=comment.post.id)

    return render(request, 'edit_comment.html', {'comment': comment})


# ❌ DELETE COMMENT
@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if comment.user == request.user:
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', id=post_id)

    return redirect('home')


# 👥 FOLLOW / UNFOLLOW
@login_required
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)

    if user_to_follow != request.user:
        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if not created:
            follow.delete()   # unfollow

    return redirect('home')