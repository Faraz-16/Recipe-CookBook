from django.shortcuts import render,redirect
from home import views
from mongoengine import *
import datetime
from user_profile.models import Recipe,Ingredient,Image,Comment

connect("Cookbook")
# Create your views here.
def index(request):
	if 'User' in request.session:
		recipes = Recipe.objects[:9]
		return render(request,'user_profile/home.html',context={"User":request.session['User'],
			"Recipes":recipes})
	return redirect(views.login,permanent=True)

def recipes(request):
	if 'User' in request.session:
		recipes = Recipe.objects()
		return render(request,'user_profile/recipes.html',context={"Recipes":recipes})
	return redirect(views.login,permanent=True)

def myrecipes(request):
	if 'User' in request.session:
		recipes = Recipe.objects(author_name=str(request.session['User']))
		return render(request,'user_profile/my_recipes.html',context={"Recipes":recipes})
	return redirect(views.login,permanent=True)


def addrecipe(request):
	if 'User' in request.session:
		if request.method == "POST":
			recipe = Recipe()
			rep_name = request.POST['recipe_name']
			image = request.FILES.get('image')
			image.name.replace(' ','_')
			img_name =str(image).replace(' ','_')
			con = request.POST['content']
			inds_names = request.POST.getlist('ind_name')
			inds_quants = request.POST.getlist('ind_quant')
			inds_units = request.POST.getlist('ind_unit')
			total = len(inds_names)
			recipe.recipe_name=rep_name
			recipe.author_name=str(request.session['User'])
			recipe.created_date=datetime.datetime.utcnow
			recipe.content=con
			recipe.image_name = str(img_name)
			for i in range(total):
				recipe.ingredients.append(Ingredient(ingredient_name=inds_names[i],
					ingredient_quant=inds_quants[i],ingredient_unit=inds_units[i]))
			recipe.save()
			img = Image(img=image)
			img.save()
			return render(request,'user_profile/add_recipe.html',
				context={"Success":"Recipe Successfully Added"})
		return render(request,'user_profile/add_recipe.html')
	return redirect(views.login,permanent=True)

def show(request,value):
	if 'User' in request.session:
		if request.method =="POST":
			recipe = Recipe.objects(recipe_name=value)[0]
			comment = request.POST['comment_name']
			recipe.comments.append(Comment(content=comment,auth_name=str(request.session['User']),
                                                       created_date=datetime.datetime.utcnow))
			recipe.save()
			return render(request,'user_profile/show_recipe.html',context={'Recipe':recipe})

		recipe = Recipe.objects(recipe_name=value)[0]
		return render(request,'user_profile/show_recipe.html',context={'Recipe':recipe})

	return redirect(views.login,permanent=True)


def delete(request,value):
	if 'User' in request.session:
		recipe = Recipe.objects(author_name=str(request.session['User']),recipe_name=value)
		recipe.delete()
		return redirect(myrecipes,permanent=True)
	return redirect(views.login,permanent=True)

def logout(request):
	if 'User' in request.session:
		del request.session['User']
		return redirect(views.login,permanent=True)
	return render(request,'home/login.html')
