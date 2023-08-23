#!/usr/bin/env python3
"""Most Recently Used caching module"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU caching class"""
    def __init__(self):
        """The initialization method"""
        super().__init__()
        self.MRU_list = []

    def put(self, key, item):
        """Method to insert items into cache"""
        if key and item:
            if key in self.MRU_list:
                self.MRU_list.remove(key)
            self.MRU_list.append(key)
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            last_idx = len(self.MRU_list) - 2
            to_discard = self.MRU_list.pop(last_idx)
            del self.cache_data[to_discard]
            print("DISCARD:", to_discard)

    def get(self, key):
        """Method to retrieve items from cache"""
        val = self.cache_data.get(key)
        if key and key in self.MRU_list:
            self.MRU_list.remove(key)
        self.MRU_list.append(key)
        return val
