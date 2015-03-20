import user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from forms import UserForm, UserProfileForm, PatternForm
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


def index_popular(request):
    context_dict = {}

    popular_patterns = Pattern.objects.filter().order_by('-views')[:20]
    context_dict['popular_patterns'] = popular_patterns

    return render(request, 'yarntail/index_popular.html', context_dict)

def index_latest(request):
    context_dict = {}

    latest_patterns = Pattern.objects.filter().order_by('-creation_date')[:20]
    context_dict['latest_patterns'] = latest_patterns

    return render(request, 'yarntail/index_latest.html', context_dict)

def index_all(request):
    context_dict = {}

    all_patterns = Pattern.objects.filter().order_by('-creation_date')
    context_dict['patterns_all'] = all_patterns

    return render(request, 'yarntail/index_all.html', context_dict)


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
        return index_popular(request)
    else:
        form = UserProfileForm(request.GET)

    return render(request, 'yarntail/profile_registration.html', {'profile_form': form})

@login_required
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

        return index_popular(request)
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

    print "got to increment statement"
    pattern.views += 1
    pattern.save()

    context_dict['user'] = user
    context_dict['pattern'] = pattern
    context_dict['views'] = pattern.views
    return render(request, 'yarntail/pattern.html', context_dict)

@login_required
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
            return index_popular(request)
        return render(request, 'yarntail/add_pattern.html', {'pattern_form': form})
    else:
        return redirect(index_popular(request))


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

