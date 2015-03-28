
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from forms import UserProfileForm, PatternForm, CommentForm
from models import *
from haystack.query import SearchQuerySet



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
def profile(request, username):
    u = User.objects.get(username=username)
    context_dict = {}

    try:
        user_profile = UserProfile.objects.get(user=u)
    except:
        user_profile = None

    patterns = Pattern.objects.filter(user=u).order_by('-views')

    context_dict['u'] = u
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
        return render(request, 'registration/registration_complete.html')
    else:
        form = UserProfileForm(request.GET)

    return render(request, 'yarntail/profile_registration.html', {'profile_form': form})


@login_required
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

        return redirect('profile', profile.user)
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

    pattern.views += 1
    pattern.save()

    context_dict['u'] = user

    context_dict['pattern'] = pattern
    context_dict['views'] = pattern.views

    context_dict['comment'] = comment

    if request.user.is_authenticated():
        form = CommentForm(request.GET)
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.pattern = Pattern.objects.get(slug=pattern_slug)
                comment.save()
            else:
                print form.errors

    return render(request, 'yarntail/pattern.html', context_dict)


def edit_pattern(request, username_slug, pattern_slug):
    c = {}
    context_dict = {}
    if request.user.is_authenticated():
        pattern = Pattern.objects.get(slug=pattern_slug)
        form = PatternForm(request.POST, instance=pattern)
        if request.method == 'POST':
            context_dict['csrf_token'] = c.update(csrf(request))
            form = PatternForm(request.POST, instance=pattern)
            print "user authenticated"
            if form.is_valid():
                print "form valid"
                patternform = form.save(commit=False)
                patternform.user = User.objects.get(id=request.user.id)
                patternform.save()
            else:
                print form.errors
            return redirect('pattern', pattern.user, pattern.slug)
        context_dict['pattern_form'] = form
        context_dict['pattern'] = pattern
        context_dict['u'] = request.user
        return render(request, 'yarntail/edit_pattern.html', context_dict)
    else:
        return redirect(index_popular(request))


@login_required
def add_pattern(request):
    c = {}
    context_dict = {}
    pattern = None
    if request.user.is_authenticated():
        form = PatternForm(request.GET)
        if request.method == 'POST':
            context_dict['csrf_token'] = c.update(csrf(request))
            form = PatternForm(request.POST)

            if form.is_valid():
                pattern = form.save(commit=False)
                pattern.user = User.objects.get(id=request.user.id)
                pattern.save()

            else:
                print form.errors
            try:
                return redirect('pattern', pattern.user, pattern.slug)
            except:
                return handle404(request)
        context_dict['pattern_form'] = form
        return render(request, 'yarntail/add_pattern.html', context_dict)
    else:
        return redirect(index_popular(request))


def what_is_yarntail(request):
    return render(request, 'yarntail/what_is_yarntail.html')


def upload_instructions(request):
    return render(request, 'yarntail/upload_instructions.html')


def get_patterns(max_results=0, contains=''):
    pattern_list = []
    if contains:
        pattern_list = Pattern.objects.filter(title__contains=contains)

    if max_results > 0:
        if len(pattern_list) > max_results:
            pattern_list = pattern_list[:max_results]
    return pattern_list

@csrf_exempt
def search_autocomplete(request):#make compatible with users

    final_results = {}
    patterns = []
    users = []
    p=None
    u=None
    query = request.POST['search_text']



    if query:

        query_results = SearchQuerySet().autocomplete(content_auto=query)
        for result in query_results:
            try:
                p = Pattern.objects.get(pk=result.pk)
                if query.lower() not in p.lower():
                    p = None
            except:
                pass

            try:
                u = UserProfile.objects.get(pk=result.pk)
                if query.lower() not in u.user.username.lower():
                    u = None
            except:
                pass

            if u != None:
                users.append({'name': u.user.username, 'url': u.get_absolute_url()})
            if p != None:
                patterns.append({'title': p.title, 'url': p.get_absolute_url()})
            u = p = None

        final_results['patterns'] = patterns
        final_results['users'] = users

    return JsonResponse(final_results, safe=False)


def search_results(request):
    context_dict = {}
    patterns = []
    users = []
    p=None
    u=None
    query = request.GET.urlencode().replace("search=", "")
    if query:
        query_results = SearchQuerySet().filter(text=query)



        for result in query_results:
            try:
                p = Pattern.objects.get(pk=result.pk)
                if query.lower() not in p.lower():
                    p = None
            except:
                pass

            try:
                u = UserProfile.objects.get(pk=result.pk)
                if query.lower() not in u.user.username.lower():
                    u = None
            except:
                pass

            if u != None:
                users.append(u)
            if p != None:
                patterns.append(p)
            u = p = None

            context_dict['users'] = users
            context_dict['patterns'] = patterns
            context_dict['num_users'] = len(users)
            context_dict['num_patterns'] = len(patterns)
            context_dict['num_all'] = len(patterns) + len(users)

    return render(request, "yarntail/search_results.html", context_dict)



def edit_pattern(request, username_slug, pattern_slug):
    c = {}
    context_dict = {}
    print "in edit pattern"
    if request.user.is_authenticated():
        print "request="+request
        
        ##pattern = Pattern.objects.get(
        form = PatternForm(request.POST, instance=pattern)
        if request.method == 'POST':
            context_dict['csrf_token'] = c.update(csrf(request))
            form = PatternForm(request.POST)

            if form.is_valid():
                pattern = form.save(commit=False)
                pattern.user = User.objects.get(id=request.user.id)
                print "form is valid"
                pattern.save()

            else:
                print form.errors
                return HttpResponse("Oh Shiz, yo pattern is dope. (And by that we mean the form is not valid.)")
            return redirect('pattern', pattern.user, pattern.slug)
        context_dict['pattern_form'] = form
        return render(request, 'yarntail/add_pattern.html', context_dict)
    else:
        return redirect(index_popular(request))




def handle404(request):
    return render(request, "yarntail/page_not_found.html")
