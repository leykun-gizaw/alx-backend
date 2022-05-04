#!/usr/bin/env python3
""" Module defines `FIFOCache` class
"""
from typing import Any
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class

    Attributes:
        cache_data: a dictionary representation of in-memory cache
        MAX_ITEMS: an integer representing size of cache_data
    """
    def __init__(self):
        """Initialize"""
        super(FIFOCache, self).__init__()

    def put(self, key: Any, item: Any) -> None:
        """Insert cache entry (key: value) to internal dictionary

        If MAX_ITEMS is passed make sure FIFO is enforced
        """
        if key and item is not None:
            try:
                if len(self.cache_data) < self.__class__.MAX_ITEMS:
                    self.cache_data[key] = item
                elif self.cache_data.get(key) is not None:
                    self.cache_data[key] = item
                else:
                    raise Exception
            except Exception:
                first_in_key = list(self.cache_data.items())[0][0]
                self.cache_data.pop(
                        first_in_key
                        )
                print("DISCARD: {}".format(first_in_key))
                self.cache_data[key] = item

    def get(self, key) -> Any:
        """Retrieve value using key"""
        return self.cache_data.get(key)
    pass
