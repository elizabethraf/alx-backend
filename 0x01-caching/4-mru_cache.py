#!/usr/bin/python3
"""class MRUCache that inherits from BaseCaching"""
from datetime import datetime
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Display self.cache_data - dictionary from the parent class"""
    def __init__(self):
        super().__init__()
        self.usage_data = {}

    def put(self, key, item):
        """Must assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent_key = max(self.usage_data, key=self.usage_data.get)
            del self.cache_data[most_recent_key]
            del self.usage_data[most_recent_key]
            print("DISCARD: {}".format(most_recent_key))

        self.cache_data[key] = item
        self.usage_data[key] = datetime.now()

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.usage_data[key] = datetime.now()
        return self.cache_data[key]
