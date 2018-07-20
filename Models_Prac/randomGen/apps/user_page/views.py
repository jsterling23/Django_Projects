# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..logReg.models import User
from ..home.models import Thought

# Create your views here.

def index(req):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first")
        return redirect('logReg:index')
    else:
        template = 'user_page/index.html'

        user = User.objects.get(id=req.session['user_id'])
        thoughts = Thought.objects.filter(user=user)
        context = {
            'user_thoughts':thoughts,
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
    
    return redirect('user_page:index')
