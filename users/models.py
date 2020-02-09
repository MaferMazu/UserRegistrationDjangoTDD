from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
	## BASE ##
	email = models.CharField(max_length=100, null = True)
	password = models.CharField(max_length=100, null = True)

