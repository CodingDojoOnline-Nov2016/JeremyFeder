from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
    def register(self, email):
        errors = []
        if len(email) == 0:
            errors.append("You must enter an Email Address")
        elif not EMAIL_REGEX.match(email):
            errors.append("This Email Address appears to be invalid")
        ## Make sure email is unique
        # elif email == checkEmail:
        #     errors.append("An Email Address by that name already exists!  Try a new one.")
        if errors:
            return (False, errors)
        else:
            e = Email.emailManage.create(email=email)
            e.save()
            return (True, e)

    def destroy(self, id):
        e = Email.emailManage.get(id=id)
        e.delete()

class Email(models.Model):
    email = models.CharField(max_length = 80)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    emailManage = EmailManager()
