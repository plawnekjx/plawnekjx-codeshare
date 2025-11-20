from django.core.cache import cache
import requests


def get_latest_plawnekjx_release():
    CACHE_KEY = "plawnekjx-releases"
    results = cache.get(CACHE_KEY)
    if results:
        return results

    try:
        response = requests.get(
            "https://api.github.com/repos/plawnekjx/plawnekjx/releases"
        ).json()
        release_tags = [x["tag_name"] for x in response]
        cache.set(CACHE_KEY, release_tags, 3600)
        return release_tags[0]
    except:
        return ""
