#!/usr/bin/env python3
""" create LIFOCache class """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class to sort data in cashing with LIFO system """
    def __init__(self):
        """ create a constructor """
        super().__init__()

    def put(self, key, item):
        """ create put to put items in LIFO system """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data.keys()):
                last_key = ''
                for i in self.cache_data.keys():
                    last_key = i
                print(f'DISCARD: {last_key}')
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """ get specific data linked to givin key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
