from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import User, Profile
from forms import UserForm, ProfileForm


def home(request):
    users = User.objects.filter()
    for user in users:
        #TODO This is not transparent solution
        if user.id < 11:
            db_name = 'profile1'
        else:
            db_name = 'profile2'
        user.profile = Profile.objects.using(db_name).get(user_id=user.id)
    return render(request, "home.html",
                  {'users': users, 'userform': UserForm, 'profileform': ProfileForm})


def add_user(request):
    p = request.POST

    if 'name' in p and p['name'] and\
       'email' in p and p['email'] and\
       'address' in p and p['address']:
        u = User(name=p['name'])
        u.save()
        p = Profile(user_id=u.id, email=p['email'], address=p['address'])
        p.save()
    return HttpResponseRedirect(reverse("core.views.home"))


def del_user(request, del_id):
    User.objects.get(pk=del_id).delete()
    #TODO This is not transparent solution
    if int(del_id) < 11:
        db_name = 'profile1'
    else:
        db_name = 'profile2'
    Profile.objects.using(db_name).get(user_id=del_id).delete()
    return HttpResponseRedirect(reverse("core.views.home"))
