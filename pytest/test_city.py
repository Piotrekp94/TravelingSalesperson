import pytest

from city import *


@pytest.mark.parametrize(
    "city1,city2,expected",
    [(City(1, 2), City(1, 2), 0),
     (City(2, 3), City(4, 5), 2.8284271247461903)],
)
def test_distanceBetweenCities(city1, city2, expected):
    assert distanceBetweenCities(city1, city2) == expected


@pytest.mark.parametrize(
    "citieslist,expectedDistance",
    [([City(1, 2), City(1, 2)], 0),
     ([City(0, 1), City(0, 2), City(0, 3)], 2),
     ([City(1, 1), City(1, 2), City(1, 3)], 2),
     ([City(12, 1), City(167, 2163), City(139, 367)], 3963.767326267787),
     ([City(2, 3), City(4, 5)], 2.8284271247461903)]
)
def test_calculateDistance(citieslist, expectedDistance):
    assert calculateDistance(citieslist) == expectedDistance
