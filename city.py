import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calculateDistance(cities_list) :
    totalDistance = 0
    for n in range (len(cities_list) - 1) :
        totalDistance += distanceBetweenCities(cities_list[n], cities_list[n + 1])
    return totalDistance

def distanceBetweenCities(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)