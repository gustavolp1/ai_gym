from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
from time import *
import copy

class AspiradorPo10x10NoDir(State):

    def __init__(self, op, posx, posy, table):
        self.operator = op
        self.posx = posx
        self.posy = posy
        self.table = table
    
    def successors(self):
        successors = []

        #movement
        if self.posx > 0:
            successors.append(AspiradorPo10x10NoDir("move-left", self.posx-1, self.posy, self.table))
        if self.posx < 9:
            successors.append(AspiradorPo10x10NoDir("move-right", self.posx+1, self.posy, self.table))
        if self.posy > 0:
            successors.append(AspiradorPo10x10NoDir("move-up", self.posx, self.posy-1, self.table))
        if self.posy < 9:
            successors.append(AspiradorPo10x10NoDir("move-down", self.posx, self.posy+1, self.table))
        
        #cleaning
        if self.table[self.posx][self.posy] == "dirty":
            table2 = copy.deepcopy(self.table)
            table2[self.posx][self.posy] = "clean"
            successors.append(AspiradorPo10x10NoDir("clean", self.posx, self.posy, table2))

        return successors
    
    def is_goal(self):
        goal_table = []
        for i in range(0,10):
            goal_table.append([])
            for j in range(0,10):
                goal_table[i].append("clean")

        if self.table == goal_table:
            return True
        else:
            return False
    
    def description(self):
        return "Vacuum cleaner agent for a 10x10 environment"
    
    def cost(self):
        return 1
    
    def env(self):
        return f'Action: {self.operator}\nVacuum cleaner position: X={self.posx}, Y={self.posy}\nDirection: {self.dir}\nState:\n{self.table}\nEtapa'



def main():
    print('\nVacuum Cleaner 10x10 Agent\n')

    table = []
    for i in range(0,10):
        table.append([])
        for j in range(0,10):
            table[i].append("clean")

    while True:
        print("\nNew tile!\nInput a dirty tile X coordinate (0-9).\nType 'done' when finished.")
        x = input()
        if x == "done":
            break
        else:
            x = int(x)
        print("Input a dirty tile Y coordinate (0-9).")
        y = int(input())
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("Invalid coordinates. Try again.\n")
        else:
            table[x][y] = "dirty"

    while True:
        print("\nX coordinate for vacuum:")
        x = int(input())
        print("Y coordinate for vacuum:")
        y = int(input())
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("Invalid coordinates. Try again.")
        else:
            break

    posx = x
    posy = y

    state = AspiradorPo10x10NoDir("start", posx, posy, table)
    algorithm = BuscaLargura()
    start_time = time()

    print("\nSearching...")

    result = algorithm.search(state, trace=False)
    end_time = time()
    
    if result != None:
        print('\nSolution found!')
        print(f"\nPath: {result.show_path()}")
        print(f"\nTime: {end_time - start_time}")
    else:
        print('\nNo solution found.')

if __name__ == '__main__':
    main()