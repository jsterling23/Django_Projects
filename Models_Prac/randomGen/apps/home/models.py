# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logReg.models import User

# Create your models here.

class ThoughtManager(models.Manager):
    def Thought_Validator(self, postData):
        print('in thought manager thought validator')
        errors = {}
        if len(postData['content']) < 5:
            errors['content_length'] = "Must enter a valid thought"
        if(errors):
            return errors 

class Thought(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name='thoughts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ThoughtManager()

    def __str__(self):
        return ('Content: {}. User: {}.').format(self.content, self.user)


