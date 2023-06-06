from django.shortcuts import render, get_object_or_404
from .models import Recipe

# list view for recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {"recipes":recipes})

# detail view for each recipe
def recipe_detail(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
