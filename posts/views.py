from django.shortcuts import render, redirect
from .models import Post, Like, Comment
from profiles.models import  Profile
from .forms import PostModelForm, CommentModelForm

def all_posts(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    p_form = PostModelForm()
    c_form = CommentModelForm()
    post_added = False

    if 'submit_p_form' in request.POST:
        p_form = PostModelForm(request.POST,request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
            post_added = True

    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm()

    context = {
        'qs':qs,
        'profile':profile,
        'p_form': p_form,
        'c_form': c_form,
        'post_added': post_added,
    }
    return render(request, 'posts/main.html', context)

def post_like_or_unlike(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user = user)
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value = 'Like'
            post_obj.save()
            like.save()
    return redirect('posts:all-posts')
