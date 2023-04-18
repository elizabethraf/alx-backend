#!/usr/bin/python3
"""Class BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Display Basic Dictionary"""

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets cache"""

        return self.cache_data.get(key, None)
