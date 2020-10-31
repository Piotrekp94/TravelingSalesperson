from city import *
from geneticAlgorithm import *

import pytest


def prepareGA():
    ga = GeneticAlgorithm()
    ga.cities = [City(1, 2), City(4, 3), City(5, 6), City(7, 8)]
    ga.population = [Phenotype([0, 1, 2, 3]), Phenotype([3, 2, 0, 1])]
    return ga


def test_pickOne():
    ga = prepareGA()
    ga.calculateFitness()
    ga.normalizeFitness()

    random.seed(100)
    result = pickOne(ga.population)
    assert ga.population[0] == result
    result = pickOne(ga.population)
    assert ga.population[0] == result
    result = pickOne(ga.population)
    assert ga.population[1] == result


@pytest.mark.parametrize(
    "geneticAlgorithm,lowestDistance",
    [(prepareGA(), 2.8284271247461903)],
)
def test_integrationtest(geneticAlgorithm, lowestDistance):
    for i in range(len(geneticAlgorithm.population)):
        assert geneticAlgorithm.population[i].fitness == 0
        assert geneticAlgorithm.population[i].distance == math.inf

    geneticAlgorithm.calculateFitness()

    assert geneticAlgorithm.population[0].fitness == 0.10925400611220526
    assert geneticAlgorithm.population[1].fitness == 0.08585489861403532
    assert geneticAlgorithm.population[0].distance == 9.15298244508295
    assert geneticAlgorithm.population[1].distance == 11.647559034406951

    geneticAlgorithm.normalizeFitness()

    assert geneticAlgorithm.population[0].fitness == 0.5599642223685317
    assert geneticAlgorithm.population[1].fitness == 0.44003577763146823
    assert geneticAlgorithm.population[0].distance == 9.15298244508295
    assert geneticAlgorithm.population[1].distance == 11.647559034406951

    assert geneticAlgorithm.bestOrder == []
    assert geneticAlgorithm.shortestDistance == math.inf

    geneticAlgorithm.findLowestDistance()

    assert geneticAlgorithm.bestOrder.citiesOrder == geneticAlgorithm.population[
        0].citiesOrder
    assert geneticAlgorithm.shortestDistance == 9.15298244508295

    assert geneticAlgorithm.avgDistance == math.inf

    geneticAlgorithm.calculateAvgDistance()

    assert geneticAlgorithm.avgDistance == 10.40027073974495








def test_generateRandomCities():
    random.seed(100)

    cities = generateRandomCities(3, 10, 10)

    assert len(cities) == 3
    assert cities[0].x == 2
    assert cities[0].y == 7
    assert cities[1].x == 7
    assert cities[1].y == 2
    assert cities[2].x == 6
    assert cities[2].y == 5


def test_generateRandomPopulation():
    citiesList = [City(1, 2), City(4, 3), City(5, 6), City(7, 8)]
    random.seed(100)

    randomPopulation = generateRandomPopulation(5, citiesList)
    assert len(randomPopulation) == 5
    assert randomPopulation[0].citiesOrder == [0, 2, 3, 1]
    assert randomPopulation[1].citiesOrder == [0, 3, 2, 1]
    assert randomPopulation[2].citiesOrder == [3, 0, 1, 2]
    assert randomPopulation[3].citiesOrder == [2, 1, 3, 0]
    assert randomPopulation[4].citiesOrder == [1, 3, 0, 2]
