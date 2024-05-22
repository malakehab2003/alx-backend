#!/usr/bin/env python3
""" create FIFOCache class """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ class to implement the fifo caching technique """
    def __init__(self):
        """ create constructor """
        super().__init__()

    def put(self, key, item):
        """ create put to add items to dictionary """
        if key is not None and item is not None:
            # remove the first item if the max limit reached
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data.keys()):
                first_key = next(iter(self.cache_data))
                print(f'DISCARD: {first_key}')
                del self.cache_data[first_key]
            # add the new item
            self.cache_data[key] = item

    def get(self, key):
        """ get specific data linked to givin key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
