#!/usr/bin/env python3
"""Define get_page that takes two integer arguments"""
import csv
import math
from typing import List


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
            pass
    assert isinstance(page, int) and page > 0, "Page should be an integer greater than 0."

    assert isinstance(page_size, int) and page_size > 0, "Page should be an integer greater than 0."

    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = list(reader)

    start_index, end_index = index_range(page, page_size)
    if start_index >= len(data):
        return []

    return data[start_index:end_index]

    def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
