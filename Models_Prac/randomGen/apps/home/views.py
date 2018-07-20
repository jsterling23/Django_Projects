# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from ..home.models import *
from django.utils import timezone
import datetime


def index(req):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first")
        return redirect(reverse('logReg:index'))
    else:
        template = 'home/index.html'
        test_timezone = timezone.now()
        test_datetime = datetime.datetime.now()

        context = {
            'thoughts':Thought.objects.all(),
            'timezone':test_timezone,
            'datetime':test_datetime,
        }
        return render(req, template, context)



def add_thoughts(req):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first")
        return redirect('logReg:index')
    else:
        template = 'home/add_thought.html'
        context = {
            'thoughts':Thought.objects.all(),
        }
        return render(req, template, context) 



def process_add_thought(req):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first to add a thought...")
        return redirect(reverse('logReg:index'))
    else:
        if req.method == "POST":

            form_errors = Thought.objects.Thought_Validator(req.POST)

            if(form_errors):
                for tag, error in form_errors.items():
                    messages.error(req, error, extra_tags=tag)
                return redirect('home:add_thoughts')

            user = User.objects.get(id=req.session['user_id'])  

            Thought.objects.create(content=req.POST['content'], user=user)
            return redirect('home:index')
        else:
            messages.error(req, "You are not allowed to do this..")
            return redirect('logReg:index')



def edit_thought(req, thought_id):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first to edit a thought...")
        return redirect(reverse('logReg:index'))
    else:
        template = 'home/edit_thought.html'
        context = {
            'thought':Thought.objects.get(id=thought_id)
        }

        return render(req, template, context)



def process_edit_thought(req, thought_id):
    print('processing edit thought')
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first to edit anything...")
        return redirect(reverse('logReg:index'))

    if req.method == "POST":
        print('in req.method POST')
        edit_form_errors = Thought.objects.Thought_Validator(req.POST)
        
        if(edit_form_errors):
            for tag, error in edit_form_errors.items():
                messages.error(req, error, extra_tags=tag)
            return redirect(reverse('home:edit_thought', kwargs={'thought_id':thought_id}))
        print('past form errors check')
        thought_to_edit = Thought.objects.get(id=thought_id)
        thought_to_edit.content = req.POST['content']
        thought_to_edit.save()
     
        return redirect('home:index')
    else:
        messages.error(req, "You are not allowed to do this..")
        return redirect('logReg:index')



def delete_thought(req, thought_id):
    if 'logged_in' not in req.session:
        messages.error(req, "You need to login or register first to delete...")
        return redirect(reverse('logReg:index'))
    else:
        thought_to_delete = Thought.objects.get(id=thought_id)
        thought_to_delete.delete()
        return redirect('home:index')
        