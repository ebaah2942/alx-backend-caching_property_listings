from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property 
from django.views.decorators.csrf import csrf_exempt
from .utils import get_all_properties

# Create your views here.
@csrf_exempt
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({
        "data": properties
    })

