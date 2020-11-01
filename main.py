import pygame
import pygame.freetype

from geneticAlgorithm import *

white = (255, 255, 255)
yellow = (255, 255, 0)
violet = (136, 78, 160)


def saveResultToCsv(geneticAlgorithm):
    writer = csv.writer(open("file", 'w'))
    writer.writerow(geneticAlgorithm.cities)


def simulationForCsvgeneration():
    randomCities = generateRandomCities(100, 1000, 1000)

    geneticAlgorithm1 = GeneticAlgorithm("3Population", randomCities, 3)
    geneticAlgorithm2 = GeneticAlgorithm("10Population", randomCities, 10)
    geneticAlgorithm3 = GeneticAlgorithm("100Population", randomCities, 100)
    geneticAlgorithm4 = GeneticAlgorithm("1000Population", randomCities, 1000)
    geneticAlgorithms = [geneticAlgorithm1, geneticAlgorithm2, geneticAlgorithm3, geneticAlgorithm4]

    while True:
        for geneticAlgorithm in geneticAlgorithms:
            geneticAlgorithm.generateNextPopulation()
            if geneticAlgorithm.generationSinceLastBest > 200 and geneticAlgorithm.generationSinceLastBest != math.inf:
                saveResultToCsv(geneticAlgorithm)
                geneticAlgorithms.remove(geneticAlgorithm)
        if len(geneticAlgorithms) == 0:
            break


def simulationForGraphicVisualisation():
    geneticAlgorithm = GeneticAlgorithm("Test1", generateRandomCities(15, 1000, 1000), 100)
    screen_width = 1000
    screen_height = 1000
    backgroundColor = (0, 0, 0)

    run = True

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if geneticAlgorithm.generationSinceLastBest > 1000 and geneticAlgorithm.generationSinceLastBest != math.inf:
            saveResultToCsv(geneticAlgorithm)
            break
        geneticAlgorithm.generateNextPopulation()

        drawGraph(geneticAlgorithm, screen)
        drawData(geneticAlgorithm, screen)

        pygame.display.update()
        screen.fill(backgroundColor)


def main():
    # simulationForCsvgeneration()
     simulationForGraphicVisualisation()


def drawData(geneticAlgorithm, screen):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen.blit(myfont.render("Generation: " +
                              str(geneticAlgorithm.generation), False, (255, 0, 0)), (0, 0))
    screen.blit(myfont.render("shortestDistance: " +
                              str(geneticAlgorithm.shortestDistance), False, (255, 0, 0)), (0, 35))
    screen.blit(myfont.render("avgGenDistance: " +
                              str(geneticAlgorithm.avgDistance), False, (255, 0, 0)), (0, 70))


def drawGraph(geneticAlgorithm, screen):
    drawCitiesLocations(pygame, screen, geneticAlgorithm.cities, white)
    orderedCities = []
    for n in range(len(geneticAlgorithm.bestOrder.citiesOrder)):
        orderedCities.append(
            geneticAlgorithm.cities[geneticAlgorithm.bestOrder.citiesOrder[n]])
    drawCurrentShortestPath(pygame, screen, orderedCities, violet)


def drawCitiesLocations(pygame, screen, newCitiesOrder, color):
    for n in range(0, len(newCitiesOrder)):
        pygame.draw.circle(
            screen, color, (newCitiesOrder[n].x, newCitiesOrder[n].y), 4)


def drawCurrentShortestPath(pygame, screen, shortestPath, color):
    for n in range(len(shortestPath) - 1):
        pygame.draw.line(screen, color, (shortestPath[n].x, shortestPath[n].y), (
            shortestPath[n + 1].x, shortestPath[n + 1].y), 3)


main()
