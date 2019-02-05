from django.db import models
from mongoengine import *
# Create your models here.

connect('Cookbook')

class Members(Document):
	first_name = StringField(max_length=150)
	last_name = StringField(max_length=150)
	user_name = StringField(max_length=100)
	password = StringField(max_length=100)
	dob = StringField(max_length=100)
	email = StringField(max_length=100)
