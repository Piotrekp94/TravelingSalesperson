from city import *
from phenotype import *
import random

class Population:
    def __init__(self, size, citiesList):
        self.citiesList = citiesList
        self.populationOrder = generateRandomPopulation(size, citiesList)

def generateRandomPopulation(size, citiesList):
    population = []
    for i in range(size):
        array = []
        for j in range(len(citiesList)):
            array.append(j)
        random.shuffle(array)
        population.append(Phenotype(array))
    return population



