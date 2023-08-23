#!/usr/bin/python3
""""Least Recently Used caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """THE LRU caching class"""
    def __init__(self):
        """The constructor method"""
        super().__init__()
        self.LRU_list = []

    def put(self, key, item):
        """Method to insert items into cache"""
        if key and item:
            if key in self.LRU_list:
                self.LRU_list.remove(key)
            self.LRU_list.append(key)
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            to_discard = self.LRU_list[0]
            self.LRU_list.remove(to_discard)
            del self.cache_data[to_discard]
            print("DISCARD:", to_discard)

    def get(self, key):
        """Method to retrieve from cache"""
        val = self.cache_data.get(key)
        if key and key in self.LRU_list:
            self.LRU_list.remove(key)
        self.LRU_list.append(key)
        return val
