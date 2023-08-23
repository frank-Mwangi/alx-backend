#!/usr/bin/python3
"""First In First Out caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """The FIFO caching class"""

    def __init__(self):
        """The initialization method"""
        super().__init__()
        self.cache_key_idxs = []

    def put(self, key, item):
        """Add items to cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                to_discard = self.cache_key_idxs.pop(0)
                del self.cache_data[to_discard]
                print('DISCARD:', to_discard)
            self.cache_data[key] = item
            self.cache_key_idxs.append(key)

    def get(self, key):
        """Retrieve cache tems by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
