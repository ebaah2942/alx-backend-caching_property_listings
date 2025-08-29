from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property 

# Create your views here.
@cache_page(60 * 15)  # Cache the view for 15 minutes 
def property_list(request):
    properties = list(Property.objects.values())
    return JsonResponse({
        "data": properties
    })
