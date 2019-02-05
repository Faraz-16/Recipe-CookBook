from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='Home'),
    path('about/',views.about,name='About'),
    path('login/',views.login,name='Login'),
    path('register/',views.register,name='Register'),
    path('allrecipes/',views.allRecipes,name='All_Recipes'),
    path('show/(?P<value>\s+)$',views.show,name='Com_Show_recipe')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
