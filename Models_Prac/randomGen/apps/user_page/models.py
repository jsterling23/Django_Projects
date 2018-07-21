# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..logReg.models import User
# Create your models here.


class Bio(models.Model):
    profile_bio = models.TextField(blank=True)
    profile_birthday = models.DateTimeField(blank=True)
    profile_home_town = models.CharField(max_length=255,blank=True)
    profile_hobbies = models.TextField(blank=True)
    profile_favorite_genre = models.CharField(max_length=20, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return('Bio: {} || Birthday: {} || Home Town: {} || Hobbies: {} || Fav Music Genre: {} || User: {} ').format(self.profile_bio, self.profile_birthday, self.profile_home_town, self.profile_hobbies, self.profile_favorite_genre, self.user)
