from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    
    def __unicode__(self):
		return "{0} {1}".format(self.firstname, self.lastname)