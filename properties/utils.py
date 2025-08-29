from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try fetching from Redis
    properties = cache.get("all_properties")

    if not properties:
        # Fetch from DB if not in cache
        properties = Property.objects.all()
        # Store in Redis for 1 hour (3600 seconds)
        cache.set("all_properties", properties, 3600)

    return properties
