from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from aigyminsper.search.SearchAlgorithms import BuscaGananciosa
from aigyminsper.search.Graph import State
from datetime import datetime

@staticmethod
def createArea():
    return {
        'a':[(3,'b'),(6,'c')],
        'b':[(3,'a'),(3,'h'),(3,'k')],
        'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
        'd':[(3,'c'),(1,'f'),(1,'e')],
        'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
        'f':[(1,'g'),(1,'e'),(1,'d')],
        'g':[(2,'c'),(1,'f'),(2,'h')],
        'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
        'i':[(2,'e'),(2,'h')],
        'l':[(1,'k')],
        'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
        'm':[(2,'n'),(1,'x'),(14,'e')],
        'n':[(2,'m'),(3,'k')],
        'o':[(2,'c')],
        'p':[(2,'c')],
        'x':[(1,'m')]
    }

class Map(State):

    def __init__(self, op, pos, goal, cost_):
        self.operator = op
        self.pos = pos
        self.goal = goal
        self.cost_ = cost_
        self.area = createArea()

    def successors(self):
        successors = []
        for i in self.area[self.pos]:
            successors.append(Map(i[1], i[1], self.goal, i[0]))
        return successors

    def is_goal(self):
        if self.pos == self.goal:
            return True
        return False

    def description(self):
        return "Map solver using GS"

    def cost(self):
        return self.cost_

    def env(self):
        return f'Current state: {self.pos}; Cost: {self.cost()}'
    

def main():

    algorithm = BuscaCustoUniforme()
    state = Map('b', 'b', 'o', 0)

    print('\nSearching...')

    start_time = datetime.now()
    result = algorithm.search(state, trace=False) # Use trace=True to see the trace; pruning argument can be set to 'without', 'father-son' or 'general'.
    end_time = datetime.now()

    if result != None:
        print('\nSolution found!')
        print(result.show_path())
    else:
        print('\nSolution not found.')

    print(f'Processing time (HR:MN:SE.MS): {end_time - start_time}')
    if result != None:
        print(f'Total cost: {result.g}\n')
    else:
        print('Total cost is undefined.\n')

if __name__ == '__main__':
    main()