from city import *
from population import *
import random
import math
import copy


class GeneticAlgorithm:
    def __init__(self):
        self.cities = generateRandomCities(50, 1000, 1000)
        self.population = Population(100, self.cities)
        self.bestOrder = []
        self.shortestDistance = math.inf

    def generateNextPopulation(self):
        self.calculateFitness()
        self.normalizeFitness()
        self.findLowestDistance()
        self.nextGeneration()

    def findLowestDistance(self):
        for n in range(len(self.population.populationOrder)):
            if(self.population.populationOrder[n].distance < self.shortestDistance):
                self.bestOrder = copy.deepcopy(
                    self.population.populationOrder[n])
                self.shortestDistance = self.population.populationOrder[n].distance

    def calculateFitness(self):
        for n in range(len(self.population.populationOrder)):
            self.population.populationOrder[n].calculateFitness(self.cities)

    def normalizeFitness(self):
        sum = 0
        for n in range(len(self.population.populationOrder)):
            sum += self.population.populationOrder[n].fitness
        for n in range(len(self.population.populationOrder)):
            self.population.populationOrder[n].fitness = self.population.populationOrder[n].fitness / sum

    def nextGeneration(self):
        newPopulation = []
        for n in range(len(self.population.populationOrder)):
            newPopulation.append(pickOne(self.population))
            mutate(newPopulation[n])
        self.population.populationOrder = newPopulation

def pickOne(lista):
    index = 0
    r = random.uniform(0, 1)

    while (r > 0):
        r = r - lista.populationOrder[index].fitness
        index += 1
    return lista.populationOrder[index - 1]


def mutate(population):
    index = 0
    r = random.uniform(0, 1)

    while (r > 0):
        r = r - lista.populationOrder[index].fitness
        index += 1
    return lista.populationOrder[index - 1]


def generateRandomCities(citiesAmount, maxX, maxY):
    cities = []
    for n in range(citiesAmount):
        cities.append(City(random.randint(0, maxX),  random.randint(0, maxY)))
    return cities
