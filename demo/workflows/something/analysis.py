from dataclasses import dataclass

import numpy as np


@dataclass
class SomeData:
    a_array: np.ndarray
    b_array: np.ndarray


def generate_matrix(size):
    return np.zeros(size)


def mult_by_n(array, n):
    return SomeData(
        array,
        array * n
    )
