#!/usr/bin/python3
"""BasicCache chaching system"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """The BasicCache class"""

    def put(self, key, item):
        """save to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve from cache by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
