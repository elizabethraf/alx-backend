#!/usr/bin/python3
"""class FIFOCache that inherits from BaseCachin"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """dictionary from the parent class BaseCaching"""
    def __init__(self):
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """Must assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_key = self.key_list[0]
            del self.cache_data[first_key]
            del self.key_list[0]
            print("DISCARD: " + first_key + "\n")

        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """Return the value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
