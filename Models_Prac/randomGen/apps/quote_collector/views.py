# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from ..quote_collector.models import *

# Create your views here.

def index(req):
    template = 'quote_collector/index.html'
    context = {
        
    }
    return render(req, template, context)