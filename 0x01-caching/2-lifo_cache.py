#!/usr/bin/python3
"""Class LIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """Must assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.key_list.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
