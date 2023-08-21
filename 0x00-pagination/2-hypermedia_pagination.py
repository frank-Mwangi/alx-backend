#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """Return data from provided page"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        self.dataset()
        range = index_range(page, page_size)
        if range[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return page details in dict format"""
        dataset_items = len(self.dataset())
        data = self.get_page(page, page_size)
        page_count = math.ceil(dataset_items / page_size)

        result = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page + 1 < page_count else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": page_count
        }
        return result
