from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('', recipe_list, name='recipe-home'),
    path('recipe/<slug:recipe_slug>/', recipe_detail, name='recipe_detail'),
]