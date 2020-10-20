from city import *
import math

class Phenotype:
    def __init__(self, citiesOrder):
        self.citiesOrder = citiesOrder
        self.fitness = 0
        self.distance = math.inf

    def calculateFitness(self, citiesList):
        cityOrdered = []
        for n in range(len(self.citiesOrder)):
            cityOrdered.append(citiesList[self.citiesOrder[n]])
        self.distance = calculateDistance(cityOrdered)
        self.fitness = 1 / self.distance
