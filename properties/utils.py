from django.core.cache import cache
from .models import Property
import logging 
from django_redis import get_redis_connection

def get_all_properties():
    # Try fetching from Redis
    properties = cache.get("all_properties")

    if not properties:
        # Fetch from DB if not in cache
        properties = Property.objects.all()
        # Store in Redis for 1 hour (3600 seconds)
        cache.set("all_properties", properties, 3600)

    return properties


logger = logging.getLogger(__name__)
def get_redis_cache_metrics():
    try:
        # Connect to Redis
        conn = get_redis_connection("default")
        info = conn.info("stats")

        # Extract metrics
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses

        # Calculate hit ratio safely
        hit_ratio = hits / total_requests if total_requests > 0 else 0

        # Log metrics
        logger.info(f"Redis Cache - Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")

        return {
            "hits": hits,
            "misses": misses,
            "hit_ratio": hit_ratio
        }

    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0
        }