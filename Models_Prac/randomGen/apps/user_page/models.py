# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import birthday
from django.db import models

# Create your models here.

class Bio(models.Model):
    profile_bio = TextField()
    profile_birthday = birthday.fields.BirthdayField()
    profile_home_town = 
    profile_hobbies = 
    profile_favorite_genre = 
    user = 
    created_at = 
    updated_at = 