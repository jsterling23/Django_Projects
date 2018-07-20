# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..quote_collector.models import *

# Create your views here.
#Testing everything here

def index(req):
    template = 'logReg/logReg.html'
    context = {
        'users':User.objects.all()
    }
    return render(req, template, context)



def login(req):
    if req.method == "POST":

        form_errors = User.objects.Login_Validator(req.POST)

        if(form_errors):
            for tag, error in form_errors.items():
                messages.error(req, error, extra_tags=tag)
            return redirect(reverse('logReg:index'))
        else:
            db_errors = User.objects.Check_Password(req.POST)
            if(db_errors):
                for tag, error in db_errors.items():
                    messages.error(req, error, extra_tags=tag)
                return redirect(reverse('logReg:index'))
            else:
                return redirect('home:index')
    else:
        messages.error(req, "Nope.. Don't do that..")
        return redirect('logReg:index')



def register(req):
    if req.method == "POST":
        
        form_errors = User.objects.Register_Validator(req.POST)

        if(form_errors):
            for tag, error in form_errors.items():
                messages.error(req, error, extra_tags=tag)
            return redirect(reverse('logReg:index'))

        else:
            messages.success(req, "Thanks for registering, please check your email for an activation letter!")
            return redirect(reverse('logReg:index'))
    else:
        messages.error(req, "That isn't possible... Try something else")
        return redirect(reverse('logReg:index'))
           
    # return redirect('/')