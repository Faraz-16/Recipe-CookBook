from django.db import models
from mongoengine import *
import datetime
# Create your models here.
connect("Cookbook")
class Image(models.Model):
	img = models.ImageField(upload_to='uploads',blank=True)

class Ingredient(EmbeddedDocument):
	ingredient_name = StringField(max_length=150)
	ingredient_quant = DecimalField()
	ingredient_unit = StringField(max_length=20)

class Comment(EmbeddedDocument):
        content = StringField()
        auth_name = StringField(max_length=120)
        created_date = DateTimeField(default=datetime.datetime.utcnow)

class Recipe(Document):
	recipe_name = StringField(max_length=120)
	author_name = StringField(max_length=150)
	created_date = DateTimeField(default=datetime.datetime.utcnow)
	content = StringField()
	image_name = StringField()
	ingredients = ListField(EmbeddedDocumentField('Ingredient'))
	comments = ListField(EmbeddedDocumentField('Comment'))
