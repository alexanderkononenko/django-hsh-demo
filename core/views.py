from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from models import User, Profile
from forms import UserForm, ProfileForm

def home(request):
    users = User.objects.filter()
    for user in users:
        user.profile = Profile.objects.get(user_id=user.id)
    return render(request, "home.html", {'users': users, 'userform': UserForm, 'profileform':ProfileForm})

def add_user(request):
    """Add a new comment."""
    p = request.POST

    if p.has_key('name') and p['name'] and p.has_key('email') and p['email'] and p.has_key('address') and p['address']:
        u = User(name=p['name'])
        u.save()
        p = Profile(user_id=u.id, email=p['email'], address=p['address'])
        p.save()
    return HttpResponseRedirect(reverse("core.views.home"))