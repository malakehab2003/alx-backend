#!/usr/bin/env python3
""" Create index_range function """
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    return ((page - 1) * page_size, page * page_size)
