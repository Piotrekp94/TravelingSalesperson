import pygame
import pygame.freetype
import random
import copy
from geneticAlgorithm import *
import math


def main():
    geneticAlgorithm = GeneticAlgorithm()
    shortestPath = []
    numberOfCities = 10
    screen_width = 1000
    screen_height = 1000
    FPS = 60
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    violet = (136, 78, 160)
    backgroundColor = (0, 0, 0)
    cities = []
    citiesOrder = []
    newCitiesOrder = []
    programFinished = False
    run = True
    numberOfCheckedPaths = 0
    shortestDistance = 1.7976931348623157e+308

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill(backgroundColor)
            geneticAlgorithm.generateNextPopulation()
            drawCitiesLocations(pygame, screen, geneticAlgorithm.cities, white)
            orderedCities = []
            for n in range(len(geneticAlgorithm.bestOrder.citiesOrder)):
                orderedCities.append(
                    geneticAlgorithm.cities[geneticAlgorithm.bestOrder.citiesOrder[n]])
            drawCurrentShortestPath(
                pygame, screen, orderedCities, geneticAlgorithm.bestOrder, violet)

            pygame.display.update()


def drawCitiesLocations(pygame, screen, newCitiesOrder, color):
    for n in range(0, len(newCitiesOrder)):
        pygame.draw.circle(
            screen, color, (newCitiesOrder[n].x, newCitiesOrder[n].y), 4)


def drawCurrentShortestPath(pygame, screen, shortestPath, newCitiesOrder, color):
    for n in range(len(shortestPath) - 1):
        pygame.draw.line(screen, color, (shortestPath[n].x, shortestPath[n].y), (
            shortestPath[n + 1].x, shortestPath[n + 1].y), 3)
        pygame.draw.line(screen, color, (shortestPath[0].x, shortestPath[0].y), (shortestPath[len(
            newCitiesOrder.citiesOrder) - 1].x, shortestPath[len(newCitiesOrder.citiesOrder) - 1].y), 3)


main()