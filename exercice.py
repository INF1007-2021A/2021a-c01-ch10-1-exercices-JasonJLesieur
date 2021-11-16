#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array(np.linspace(-1.3, 2.5, num=64))


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    for i in range(len(cartesian_coordinates[0]) + 1):
        x = cartesian_coordinates[i][0]
        y = cartesian_coordinates[i][1]
        print(x, y)
        a = np.array(np.sqrt(x ** 2 + y ** 2))
        b = np.array(np.arctan2(x, y))
    return np.array([[a],[b]])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    coord = np.array([(0, 0), (10, 10), (2, -1)])
    # print(linear_values())
    coordinate_conversion(coord)
