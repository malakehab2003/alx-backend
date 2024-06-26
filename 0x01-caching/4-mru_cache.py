#!/usr/bin/env python3
""" create MRUCache class """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ class to sort data in cashing with MRU system """
    def __init__(self):
        """ create constructor """
        super().__init__()
        self.my_list = []

    def put(self, key, item):
        """ create put function to put items as in MUR cashing system """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data.keys()):
                print(f'DISCARD: {self.my_list[-1]}')
                del self.cache_data[self.my_list[-1]]
                self.my_list.remove(self.my_list[-1])
            self.cache_data[key] = item
            if key not in self.my_list:
                self.my_list.append(key)

    def get(self, key):
        """ get specific data linked to givin key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.my_list.remove(key)
        self.my_list.append(key)
        return self.cache_data[key]
