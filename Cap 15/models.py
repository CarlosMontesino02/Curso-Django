from __future__ import unicode_literals
from django.db import models

class Registrad(models.Model):
    nombre = models.Charfield(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self): #Py2
        return self.email
    def __str__(self): #Py3
        return self.email
