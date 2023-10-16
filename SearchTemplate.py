from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaProfundidadeIterativa, BuscaCustoUniforme, BuscaGananciosa
from aigyminsper.search.Graph import State
from datetime import datetime

class SearchTemplate(State): # Class name may be changed.

    def __init__(self, op):
        self.operator = op # Operator is ALWAYS required!
        # Add other attributes here. 
        # For example: 
        # self.pos = pos
        # self.goal = goal
        # (Don't forget to add them to the constructor's parameters!)

    def successors(self):
        successors = []
        # Add successors here. 
        # For example: successors.append(SearchTemplate('action_clean', self.pos, self.goal))
        return successors

    def is_goal(self):
        # Add goal test here.
        # For example:
        # if self.pos == self.goal:
        #    return True
        return False

    def description(self):
        # Write a description for your problem here.
        return "Template description"

    def cost(self):
        # If dealing with uniform cost, simply return 1.
        # Otherwise, use if-else statements to return different costs for different actions.
        return 1

    def env(self):
        # Used for trace. Make it an adequate representation of the state.
        return self.operator

def main():

    algchoice = None
    depth = None
    while algchoice != '1' and algchoice != '2' and algchoice != '3' and algchoice != '4' and algchoice != '5':
        algchoice = input('\nChoose an algorithm! (Type its number.)\n1. BFS (Breadth-First Search)\n2. DFS (Depth-First Search)\n3. IDDFS (Iterative Deepening Depth-First Search)\n4. UCS (Uniform Cost Search)\n5. GS (Greedy Search)\nYour choice: ')
        if algchoice == '1':
            algorithm = BuscaLargura()
            print('\nBFS chosen!')
        elif algchoice == '2':
            algorithm = BuscaProfundidade()
            print('\nDFS chosen!')
            depth = input('\nSpecify a depth limit: ')
        elif algchoice == '3':
            algorithm = BuscaProfundidadeIterativa()
            print('\nIDDFS chosen!')
        elif algchoice == '4':
            algorithm = BuscaCustoUniforme()
            print('\nUCS chosen!')
        elif algchoice == '5':
            algorithm = BuscaGananciosa()
            print('\nUCS chosen!')
        else:
            print('\nInvalid choice. Try again.')

    state = SearchTemplate('Start')

    print('\nSearching...')

    start_time = datetime.now()
    if depth != None:
        result = algorithm.search(state, m=int(depth)) # Use trace=True to see the trace; pruning argument can be set to 'without', 'father-son' or 'general'.
    else:
        result = algorithm.search(state) # Use trace=True to see the trace; pruning argument can be set to 'without', 'father-son' or 'general'.
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