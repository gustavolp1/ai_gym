from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
from datetime import datetime

class Poi(State):

    def __init__(self, op, pos, goal):
        self.operator = op
        self.pos = pos
        self.goal = goal

    def successors(self):
        successors = []
        if self.pos == 'A':
            successors.append(Poi('A->B', 'B', self.goal))
            successors.append(Poi('A->C', 'C', self.goal))
        if self.pos == 'B':
            successors.append(Poi('B->A', 'A', self.goal))
            successors.append(Poi('B->C', 'C', self.goal))
            successors.append(Poi('B->D', 'D', self.goal))
        if self.pos == 'C':
            successors.append(Poi('C->A', 'A', self.goal))
            successors.append(Poi('C->B', 'B', self.goal))
            successors.append(Poi('C->E', 'E', self.goal))
        if self.pos == 'D':
            successors.append(Poi('D->B', 'B', self.goal))
            successors.append(Poi('D->E', 'E', self.goal))
        if self.pos == 'E':
            successors.append(Poi('E->C', 'C', self.goal))
            successors.append(Poi('E->D', 'D', self.goal))
            successors.append(Poi('E->F', 'F', self.goal))
            successors.append(Poi('E->G', 'G', self.goal))
        if self.pos == 'F':
            successors.append(Poi('F->E', 'E', self.goal))
            successors.append(Poi('F->G', 'G', self.goal))
        if self.pos == 'G':
            successors.append(Poi('G->E', 'E', self.goal))
            successors.append(Poi('G->F', 'F', self.goal))
        return successors

    def is_goal(self):
        if self.pos == self.goal:
            return True
        return False

    def description(self):
        return "Simple graph solver"

    def cost(self):
        return 1

    def env(self):
        return f'{self.operator}'

def main():
    algchoice = None
    while algchoice != '0' and algchoice != '1':
        algchoice = input('\nChoose between BFS or IDDFS (0 or 1): ')
        if algchoice == '0':
            algorithm = BuscaLargura()
            print('\nBFS chosen!')
        elif algchoice == '1':
            algorithm = BuscaProfundidadeIterativa()
            print('\nIDDFS chosen!')
        else:
            print('\nInvalid choice. Try again.')

    startpos = input('\nStarting position: ')
    goalpos = input('\nGoal position: ')

    state = Poi('Start', startpos, goalpos)
    start_time = datetime.now()
    result = algorithm.search(state, trace=True)
    end_time = datetime.now()

    if result != None:
        print('\nSolution found!')
        print(result.show_path())
    else:
        print('\nSolution not found.')

    print(f'\nTempo de processamento = {end_time - start_time}')

if __name__ == '__main__':
    main()