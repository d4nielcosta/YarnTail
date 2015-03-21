import json
import user
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms import model_to_dict
from django.shortcuts import render, redirect, render_to_response
from django.http import JsonResponse
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
            profileForm = UserProfileForm(request.POST, instance=profile)
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

    print "got to increment statement"
    pattern.views += 1
    pattern.save()

    context_dict['user'] = user
    context_dict['pattern'] = pattern
    context_dict['views'] = pattern.views
    return render(request, 'yarntail/pattern.html', context_dict)


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
            # Fix Return. We want to return pattern
            return index(request)
        return render(request, 'yarntail/add_pattern.html', {'pattern_form': form})
    else:
        return redirect(index(request))


def pattern_instructions(request):
    return render(request, 'yarntail/pattern_instructions.html')


def upload_instructions(request):
    return render(request, 'yarntail/upload_instructions.html')


def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''

    patterns = get_patterns(max_results = 10, starts_with=search_text)
    pattern_titles = []
    for pat in patterns:
        pattern_titles = pat.title

    return HttpResponse(pattern_titles, content_type="application/json")
    #return JsonResponse(json.dumps(pattern_titles), safe=False)


def get_patterns(max_results=0, starts_with=''):
    pattern_list = []
    if starts_with:
        pattern_list = Pattern.objects.filter(title__startswith=starts_with)
    if max_results > 0:
        if len(pattern_list) > max_results:
            pattern_list = pattern_list[:max_results]
    return pattern_list

def search_results(request, query=None):
    context_dict = {}
    if query:

        patterns = Pattern.objects.filter(title__contains=query)

        context_dict['patterns'] = patterns

    return render(request, "yarntail/search_results.html", context_dict)

