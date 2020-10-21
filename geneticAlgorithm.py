from city import *
from phenotype import *
import random
import math
import copy

counter = 0


class GeneticAlgorithm:
    def __init__(self):
        self.generation = 0
        self.cities = generateRandomCities(10, 1000, 1000)
        self.population = generateRandomPopulation(100, self.cities)
        self.bestOrder = []
        self.shortestDistance = math.inf
        self.avgFitness = 0

    def generateNextPopulation(self):
        self.calculateFitness()
        self.normalizeFitness()
        self.findLowestDistance()
        self.nextGeneration()
        self.generation += 1

    def findLowestDistance(self):
        for n in range(len(self.population)):
            if(self.population[n].distance < self.shortestDistance):
                self.bestOrder = copy.deepcopy(
                    self.population[n])
                self.shortestDistance = self.population[n].distance

    def calculateFitness(self):
        for n in range(len(self.population)):
            self.population[n].calculateFitness(self.cities)
            # print(self.population[n].fitness)

    def normalizeFitness(self):
        sum = 0
        for n in range(len(self.population)):
            sum += self.population[n].fitness

        self.avgFitness = sum / len(self.population)
        for n in range(len(self.population)):
            self.population[n].fitness = self.population[n].fitness / sum

    def nextGeneration(self):
        newPopulation = []
        for n in range(len(self.population)):
            phenotype = pickOne(self.population)
            phenotype.mutate()
            newPopulation.append(copy.deepcopy(phenotype))
        self.population = newPopulation


def pickOne(lista):
    index = 0
    r = random.uniform(0, 1)

    while (r > 0):
        r = r - lista[index].fitness
        index += 1
    return lista[index - 1]


def generateRandomCities(citiesAmount, maxX, maxY):
    cities = []
    for n in range(citiesAmount):
        cities.append(City(random.randint(0, maxX),  random.randint(0, maxY)))
    return cities


def generateRandomPopulation(size, citiesList):
    population = []
    for i in range(size):
        array = []
        for j in range(len(citiesList)):
            array.append(j)
        random.shuffle(array)
        population.append(Phenotype(array))
    return population
