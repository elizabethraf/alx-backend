#!/usr/bin/python3
"""class LFUCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def update_frequency(self, key):
        """Update grequently"""
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        if self.frequency[key] < self.frequency[self.min_frequency]:
            self.min_frequency = key

    def put(self, key, item):
        """Must assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.min_frequency in self.cache_data:
                del self.cache_data[self.min_frequency]
                del self.frequency[self.min_frequency]
            else:
                lru_key = min(self.frequency, key=self.frequency.get)
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.update_frequency(key)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        return self.cache_data[key]
