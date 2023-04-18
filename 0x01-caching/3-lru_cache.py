#!/usr/bin/python3
"""Class LRUCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Display self.cache_data - dictionary from the parent class"""
    def __init__(self):
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """Must assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.key_list.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.key_list.remove(key)
        self.key_list.append(key)

        return self.cache_data[key]
