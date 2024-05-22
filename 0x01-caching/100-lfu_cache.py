#!/usr/bin/env python3
""" create LFUCache class """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class to sort data in cashing with LFU system """
    def __init__(self):
        """ create constructor """
        super().__init__()
        self.my_dict = {}

    def put(self, key, item):
        """ create put function to put items as in LFU cashing system """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data.keys()):
                min_key = list(self.my_dict.keys())[0]
                min = self.my_dict[min_key]
                for k, i in self.my_dict.items():
                    if i < min:
                        min = i
                        min_key = k
                print(f'DISCARD: {min_key}')
                del self.cache_data[min_key]
                del self.my_dict[min_key]
            self.cache_data[key] = item
            if key not in self.my_dict.keys():
                self.my_dict[key] = 1
            else:
                self.my_dict[key] += 1

    def get(self, key):
        """ get specific data linked to givin key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.my_dict[key] += 1
        return self.cache_data[key]
