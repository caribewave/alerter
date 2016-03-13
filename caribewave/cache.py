import os
import settings


def make_cache_dir():
    if not os.path.exists(settings.CACHE_DIR):
        os.makedirs(settings.CACHE_DIR)
