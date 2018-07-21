# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..logReg.models import User
from ..home.models import Thought
from ..user_page.models import Bio

# Create your views here.

def index(req):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first")
        return redirect('logReg:index')
    else:
        template = 'user_page/index.html'

        user = User.objects.get(id=req.session['user_id'])
        thoughts = Thought.objects.filter(user=user)
        bio = Bio.objects.filter(user=user)

        context = {
            'user_thoughts':thoughts,
            'bio':bio,
        }
    return render(req, template, context)



def edit_bio(req):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first")
        return redirect('logReg:index')
    else:
        template = 'user_page/edit_bio.html'
        return render(req, template)



def process_edit_bio(req):
    
    bio = req.POST['profile_bio']
    birthday = req.POST['profile_birthday']
    home_town = req.POST['profile_home_town']
    hobbies = req.POST['profile_hobbies']
    genre = req.POST['profile_favorite_genre']
    user = User.objects.get(id=req.session['user_id'])

    if Bio.objects.filter(user=user).exists():
        print('where i need tobe')
        bio_update = Bio.objects.update(
            profile_bio = bio,
            profile_birthday = birthday,
            profile_home_town = home_town,
            profile_hobbies = hobbies,
            profile_favorite_genre = genre,
            user = user,
        )
        bio_update.save()

    else:
        print('not where i need to be')
        Bio.objects.create(
            profile_bio = bio,
            profile_birthday = birthday,
            profile_home_town = home_town,
            profile_hobbies = hobbies,
            profile_favorite_genre = genre,
            user = user,
        )

    print(bio, birthday, home_town, hobbies, genre, user)

    return redirect('user_page:index')
