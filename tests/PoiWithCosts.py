from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from aigyminsper.search.Graph import State
from datetime import datetime

class PoiWithCosts(State):

    def __init__(self, op, pos, goal):
        self.operator = op
        self.pos = pos
        self.goal = goal

    def successors(self):
        successors = []
        if self.pos == 'A':
            successors.append(PoiWithCosts('A->B', 'B', self.goal))
            successors.append(PoiWithCosts('A->C', 'C', self.goal))
        if self.pos == 'B':
            successors.append(PoiWithCosts('B->A', 'A', self.goal))
            successors.append(PoiWithCosts('B->C', 'C', self.goal))
            successors.append(PoiWithCosts('B->D', 'D', self.goal))
        if self.pos == 'C':
            successors.append(PoiWithCosts('C->A', 'A', self.goal))
            successors.append(PoiWithCosts('C->B', 'B', self.goal))
            successors.append(PoiWithCosts('C->E', 'E', self.goal))
        if self.pos == 'D':
            successors.append(PoiWithCosts('D->B', 'B', self.goal))
            successors.append(PoiWithCosts('D->E', 'E', self.goal))
        if self.pos == 'E':
            successors.append(PoiWithCosts('E->C', 'C', self.goal))
            successors.append(PoiWithCosts('E->D', 'D', self.goal))
            successors.append(PoiWithCosts('E->F', 'F', self.goal))
            successors.append(PoiWithCosts('E->G', 'G', self.goal))
        if self.pos == 'F':
            successors.append(PoiWithCosts('F->E', 'E', self.goal))
            successors.append(PoiWithCosts('F->G', 'G', self.goal))
        if self.pos == 'G':
            successors.append(PoiWithCosts('G->E', 'E', self.goal))
            successors.append(PoiWithCosts('G->F', 'F', self.goal))
        return successors

    def is_goal(self):
        if self.pos == self.goal:
            return True
        return False

    def description(self):
        return "Simple graph solver"

    def cost(self):
        if self.pos == 'A':
            if self.operator == 'C->A':
                return 10
        elif self.pos == 'C':
            if self.operator == 'A->C':
                return 10
            elif self.operator == 'E->C':
                return 5
        elif self.pos == 'D':    
            if self.operator == 'E->D':
                return 3
        elif self.pos == 'E':
            if self.operator == 'C->E':
                return 5
            elif self.operator == 'D->E':
                return 3
            elif self.operator == 'G->E':
                return 2
        elif self.pos == 'G':
            if self.operator == 'E->G':
                return 2
        else:
            return 1
        
        return 1

    def env(self):
        return f'{self.operator}'

def main():
    algchoice = None
    while algchoice != '0' and algchoice != '1' and algchoice != '2':
        algchoice = input('\nChoose between BFS, IDDFS or UCS (0, 1 or 2): ')
        if algchoice == '0':
            algorithm = BuscaLargura()
            print('\nBFS chosen!')
        elif algchoice == '1':
            algorithm = BuscaProfundidadeIterativa()
            print('\nIDDFS chosen!')
        elif algchoice == '2':
            algorithm = BuscaCustoUniforme()
            print('\nUCS chosen!')
        else:
            print('\nInvalid choice. Try again.')

    startpos = input('\nStarting position: ')
    goalpos = input('\nGoal position: ')

    state = PoiWithCosts('Start', startpos, goalpos)
    start_time = datetime.now()
    result = algorithm.search(state, trace=True)
    end_time = datetime.now()

    if result != None:
        print('\nSolution found!')
        print(result.show_path())
    else:
        print('\nSolution not found.')

    print(f'Processing time = {end_time - start_time}')
    print(f'Total cost = {result.g}')

if __name__ == '__main__':
    main()