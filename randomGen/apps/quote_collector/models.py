# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def Register_Validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Must Enter valid First Name"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Must Enter Valid Last Name"
        if len(postData['email']) < 2:
            errors['email'] = 'Must Enter Valid Email'
        if len(postData['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords must match!"
        if User.objects.filter(email=postData['email']).exists():
            errors['email_taken'] = "That email has already been used... Please try another email."
        if(errors):
            return errors
        else:
            db_new_passwordhash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            
            User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=db_new_passwordhash.decode('utf-8'),
            )

    def Login_Validator(self, postData):
        errors = {}
        if len(postData['email']) < 2:
            errors['email'] = 'Must Enter Valid Email'
        if len(postData['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'
        if(errors):
            return errors
    
    def Check_Password(self, postData):
        errors = {}
        if User.objects.filter(email=postData['email']).exists():
            user = User.objects.get(email=postData['email'])
            print(user)
        else:
            errors['email_does_not_exist'] = "That email or password doesn't exist"
            return errors
        # captured the db password related to the email address in the db
        db_password = user.password

        if bcrypt.checkpw(postData['password'].encode(), db_password.encode()) == False:
            errors['password_validation_fail'] = "Password or Email was incorrect"
            return errors
        else:
            return
      

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return ( 'First Name: {}... Last Name: {}... Email: {}...' ).format(self.first_name,self.last_name,self.email)

class Quote(models.Model):
    content = models.TextField(max_length=255)
    user = models.ForeignKey(User, related_name='quotes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ( 'user: {}... content: {}...' ).format(self.user,self.content)




    