from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',views.index,name='User'),
    path('my_recipes/',views.myrecipes,name='My_recipes'),
    path('add_recipe/',views.addrecipe,name='Add_recipe'),
    path('logout/',views.logout,name='Logout'),
    path('recipes/',views.recipes,name='Recipes'),
    path('shows/(?P<value>\s+)$',views.show,name='Show_recipe'),
    path('delete/(?P<value>\s+)$',views.delete,name='Delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
