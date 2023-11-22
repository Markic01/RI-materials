import random

class Individual:
    def __init__(self,cost,fixed) -> None:
        pass
    def calcFitness(self,x,y):
        pass
    
def selection():
    pass

def crossover():
    pass
def mutation():
    pass


cost = []
fixedCost = []

POPULATION_SIZE = 100
NUM_GENERATIONS = 10
ELITISIM_SIZE = POPULATION_SIZE // 5

population = [Individual(cost, fixedCost) for _ in range(POPULATION_SIZE)]
newPopulation = [Individual(cost, fixedCost) for _ in range(POPULATION_SIZE)]

for i in range(NUM_GENERATIONS):
    population.sort(reverse=True) # < mora ima __lt__ operator
    newPopulation[:ELITISIM_SIZE] = population[:ELITISIM_SIZE]
    for j in range(ELITISIM_SIZE, POPULATION_SIZE, 2):
        parent1Index = selection(population)
        parent2Index = selection(population)
        
        crossover(population[parent1Index], population[parent2Index], newPopulation[j], newPopulation[j+1])
        
        mutation(newPopulation[j])
        mutation(newPopulation[j+1])
        
    population = newPopulation
    
best = max(population)

