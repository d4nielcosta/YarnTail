import user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from forms import UserForm, UserProfileForm, PatternForm, CommentForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from models import *

"""
+Search
+Trending
-Profile Pic
-Profile Name
-Likes
-Favorites
-Activity Feed
-Patterns Directory
-Upload New Pattern Link
"""


def index(request):
    context_dict = {}

    latest_patterns = Pattern.objects.filter().order_by('-creation_date')[:20]
    context_dict['latest_patterns'] = latest_patterns

    popular_patterns = Pattern.objects.filter().order_by('-views')[:20]
    context_dict['popular_patterns'] = popular_patterns

    return render(request, 'yarntail/index.html', context_dict)


def about(request):

    return render(request, 'yarntail/about.html')

@login_required
def profile(request, username_slug):
    u = User.objects.get(username=username_slug)
    context_dict = {}

    try:
        user_profile = UserProfile.objects.get(user=u)
    except:
        user_profile = None

    patterns = Pattern.objects.filter(user=u).order_by('-views')

    context_dict['user'] = u
    context_dict['userprofile'] = user_profile
    context_dict['patterns'] = patterns

    return render(request, 'yarntail/profile.html', context_dict)


def register_profile(request):
    if request.method == 'POST':
        try:
            userProfile = UserProfile.objects.get(user=request.user)
            form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        except:
            form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated():
                profile = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                profile.user = user
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
        else:
            print form.errors
        return index(request)
    else:
        form = UserProfileForm(request.GET)

    return render(request, 'yarntail/profile_registration.html', {'profile_form': form})


def edit_profile(request):
    if request.method == "POST":

        try:
            profile = UserProfile.objects.get(user=request.user)
            profileForm = UserProfileForm(request.POST, instance = profile)
        except:
            profileForm = UserProfileForm(request.POST)

        if profileForm.is_valid():

            if request.user.is_authenticated():
                profile = profileForm.save(commit=False)
                user = request.user
                profile.user = user

                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
        else:
            print profileForm.errors

        return index(request)
    else:
        profileForm = UserProfileForm(request.GET)

    context_dict = {}
    context_dict['profile'] = profileForm

    return render(request, 'yarntail/edit_profile.html', context_dict)

def pattern(request, username_slug, pattern_slug):
    username = username_slug.lower()
    context_dict = {}
    profile = UserProfile.objects.get(slug=username)
    user = User.objects.get(user_profile=profile)
    pattern = Pattern.objects.get(user=user, slug=pattern_slug)
    comment = Comment.objects.filter(pattern=pattern).order_by('-creation_date')

    print "got to increment statement"
    pattern.views += 1
    pattern.save()

    context_dict['user'] = user
    context_dict['pattern'] = pattern
    context_dict['views'] = pattern.views
    context_dict['comment'] = comment
    return render(request, 'yarntail/pattern.html', context_dict)

def comment(request, username_slug, pattern_slug):
    username = username_slug.lower()
    context_dict = {}
    profile = UserProfile.objects.get(slug=username)
    pattern = Pattern.objects.get(slug=pattern_slug)

    context_dict['user'] = profile
    context_dict['pattern'] = pattern

    if request.user.is_authenticated():
        form = CommentForm(request.GET)
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = User.objects.get(username=username_slug)
                comment.pattern = Pattern.objects.get(slug=pattern_slug)
                comment.save()
            else:
                print form.errors

            return index(request)
        return render(request, 'yarntail/comment.html', {'comment_form': form})
    else:
        return redirect(pattern(request, username_slug, pattern_slug))


def add_pattern(request):
    if request.user.is_authenticated():
        form = PatternForm(request.GET)
        if request.method == 'POST':
            form = PatternForm(request.POST)
            if form.is_valid():
                pattern = form.save(commit=False)
                pattern.user = User.objects.get(id=request.user.id)
                pattern.save()
            else:
                print form.errors
            #Fix Return. We want to return pattern
            return index(request)
        return render(request, 'yarntail/add_pattern.html', {'pattern_form': form})
    else:
        return redirect(index(request))


def pattern_instructions(request):

    return render(request, 'yarntail/pattern_instructions.html')


def upload_instructions(request):

    return render(request, 'yarntail/upload_instructions.html')



def search(request):

    qs = User.objects.all()
    qs = User.objects.get(username=request.user.username)
    for term in query_name.split():
        qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
        return

    return render(request, 'yarntail/search.html', qs)

