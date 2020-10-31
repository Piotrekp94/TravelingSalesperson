import copy
import csv
import os

from phenotype import *


class GeneticAlgorithm:
    def __init__(self, name):
        self.generation = 0
        self.cities = generateRandomCities(10, 1000, 1000)
        self.population = generateRandomPopulation(100, self.cities)
        self.bestOrder = []
        self.generationSinceLastBest = math.inf
        self.avgDistance = math.inf
        self.shortestDistance = math.inf
        self.avgFitness = 0
        self.name = name
        self.thisGenerationShortestDistance = math.inf

        if os.path.exists(self.name + ".csv"):
            os.remove(self.name + ".csv")
        writer = csv.writer(open(self.name + ".csv", 'a', newline=''))
        writer.writerow(['AvgDistance', 'LowestDistanceThisGen', 'LowestDistance'])

    def generateNextPopulation(self):
        self.thisGenerationShortestDistance = math.inf
        self.calculateFitness()
        self.normalizeFitness()
        self.findLowestDistance()
        self.calculateAvgDistance()
        self.nextGeneration()
        self.generationSinceLastBest = self.generationSinceLastBest + 1
        self.generation += 1
        self.saveToCsv()

    def findLowestDistance(self):
        for n in range(len(self.population)):
            if self.population[n].distance < self.shortestDistance:
                self.bestOrder = copy.deepcopy(
                    self.population[n])
                self.generationSinceLastBest = 0
                self.shortestDistance = self.population[n].distance
            if self.population[n].distance < self.thisGenerationShortestDistance:
                self.thisGenerationShortestDistance = self.population[n].distance

    def calculateFitness(self):
        for n in range(len(self.population)):
            self.population[n].calculateFitness(self.cities)

    def calculateAvgDistance(self):
        sumDistance = 0
        for n in range(len(self.population)):
            sumDistance += self.population[n].distance
        self.avgDistance = sumDistance / len(self.population)

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
            self.population.sort(key=lambda x: x.fitness, reverse=True)
            phenotypeX = pickBestFromRange(self.population, 0.1)
            phenotypeY = pickBestFromRange(self.population, 0.1)
            phenotype = crossover(phenotypeX, phenotypeY)
            phenotype.mutate()
            newPopulation.append(copy.deepcopy(phenotype))
        self.population = newPopulation

    def saveToCsv(self):
        writer = csv.writer(open(self.name + ".csv", 'a', newline=''))
        writer.writerow([round(self.avgDistance, 2), round(self.thisGenerationShortestDistance, 2),
                         round(self.shortestDistance, 2)])


def pickBestFromRange(list, range):
    index = 0
    r = random.uniform(0, range)

    while r > 0:
        r = r - list[index].fitness
        index += 1
    return list[index - 1]


# Not used
def pickOne(list):
    index = 0
    r = random.uniform(0, 1)

    while r > 0:
        r = r - list[index].fitness
        index += 1
    return list[index - 1]


def generateRandomCities(citiesAmount, maxX, maxY):
    cities = []
    for n in range(citiesAmount):
        cities.append(City(random.randint(0, maxX), random.randint(0, maxY)))
    return cities


def generateRandomPopulation(size, citiesList):
    population = []
    for i in range(size):
        array = []
        for j in range(len(citiesList)):
            array.append(j)
        random.shuffle(array)
        population.append(Phenotype(copy.deepcopy(array)))
    return population


def crossover(phenotypeX, phenotypeY):
    start = random.randint(0, len(phenotypeX.citiesOrder) - 1)
    end = random.randint(start, len(phenotypeX.citiesOrder) - 1)
    citiesOrder = phenotypeX.citiesOrder[start:end]
    for n in range(0, len(phenotypeX.citiesOrder)):
        temp = phenotypeY.citiesOrder[n]
        if temp not in citiesOrder:
            citiesOrder.append(temp)
    return Phenotype(citiesOrder)
