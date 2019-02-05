from django.shortcuts import render,redirect
from mongoengine import *
from home.models import Members
from user_profile import views as I
from user_profile.models import Recipe,Comment
import datetime
# Create your views here.
def index(request):
	if 'User' in request.session:
		return redirect(I.index,permanent=True)
	recipes = Recipe.objects[:12]
	return render(request,'home/home.html',context={"Recipes":recipes})

def allRecipes(request):
	recipes = Recipe.objects()
	return render(request,'home/recipes.html',context={"Recipes":recipes})

def login(request):
	if request.method == 'POST':
		connect('Cookbook')
		user = Members.objects(user_name=request.POST['user_name'],password=request.POST['password'])[0]
		if(len(user)!=0):
			request.session['User'] = user.user_name
			return redirect(I.index,permanent=True)
		else:
			return render(request,'home/login.html',context={"Data":"User Does Not Exist!, Please Try again or Register."})
	return render(request,'home/login.html')

def register(request):
	if request.method == 'POST':
		connect('Cookbook')
		member = Members()
		member.first_name = request.POST['first_name']
		member.last_name = request.POST['last_name']
		member.user_name = request.POST['user_name']
		member.password = request.POST['password']
		member.email = request.POST['email']
		member.dob = request.POST['date']
		member.save()
		return redirect(login,permanent=True)
	return render(request,'home/register.html')

def about(request):
        return render(request,'home/about.html')

def show(request,value):
        if request.method =="POST":
                recipe = Recipe.objects(recipe_name=value)[0]
                comment = request.POST['comment_name']
                recipe.comments.append(Comment(content=comment,auth_name='Anonymous',
                                                created_date=datetime.datetime.utcnow))
                recipe.save()
        recipe = Recipe.objects(recipe_name=value)[0]
        return render(request,'home/show_recipe.html',context={'Recipe':recipe})
