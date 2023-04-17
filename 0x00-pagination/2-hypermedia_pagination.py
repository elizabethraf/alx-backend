#!/usr/bin/env python3
"""Display Implement a get_hyper method"""
import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page, page_size):
    """Return a tuple of size two containing a start index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Define method named get_page that takes two integer arguments"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Display get_hyper method that takes the same arguments"""
        data = self.get_page(page, page_size)
        dataSet = self.__dataset
        lenSet = len(dataSet) if dataSet else 0
        totalPages = math.ceil(lenSet / page_size) if dataSet else 0
        page_size = len(data) if data else 0
        prevPage = page - 1 if page > 1 else None
        nextPage = page + 1 if page < totalPages else None
        hyperMedia = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextPage,
            'prev_page': prevPage,
            'total_pages': totalPages
        }

        return hyperMedia
