#!/usr/bin/env python3
""" create BasicCache class """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ get and put data in a dictionary """
    def put(self, key, item):
        """ use self.cache_data - dictionary from the parent class BaseCaching """
        if key is not None and item is not None:
           self. cache_data[key] = item

    def get(self, key):
        """ get data from self.cache_data - dictionary of specific key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
