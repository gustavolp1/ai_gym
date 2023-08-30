from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa, BuscaLargura
from aigyminsper.search.Graph import State
from time import *

class AspiradorPo2x2Poltrona(State):

    def __init__(self, op, pos, left, right, up, down):
        # You must use this name for the operator!
        self.operator = op
        self.pos = pos
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    
    def successors(self):
        successors = []

        #movement
        successors.append(AspiradorPo2x2Poltrona("left", "l", self.left, self.right, self.up, self.down))
        successors.append(AspiradorPo2x2Poltrona("right", "r", self.left, self.right, self.up, self.down))
        if self.pos != "d":
            successors.append(AspiradorPo2x2Poltrona("up", "u", self.left, self.right, self.up, self.down))
        if self.pos != "u":
            successors.append(AspiradorPo2x2Poltrona("down", "d", self.left, self.right, self.up, self.down))
        
        #flip dirty couches
        if self.pos == "l" and self.left == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, "flipped-dirty", self.right, self.up, self.down))
        if self.pos == "r" and self.right == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, self.left, "flipped-dirty", self.up, self.down))
        if self.pos == "u" and self.up == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, self.left, self.right, "flipped-dirty", self.down))
        if self.pos == "d" and self.down == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, self.left, self.right, self.up, "flipped-dirty"))

        #clean flipped dirty couches
        if self.pos == "l" and self.left == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, "flipped-clean", self.right, self.up, self.down))
        if self.pos == "r" and self.right == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, self.left, "flipped-clean", self.up, self.down))
        if self.pos == "u" and self.up == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, self.left, self.right, "flipped-clean", self.down))
        if self.pos == "d" and self.down == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, self.left, self.right, self.up, "flipped-clean"))

        #unflip couches
        if self.pos == "l" and self.left == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, "couch-clean", self.right, self.up, self.down))
        if self.pos == "r" and self.right == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, self.left, "couch-clean", self.up, self.down))
        if self.pos == "u" and self.up == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, self.left, self.right, "couch-clean", self.down))
        if self.pos == "d" and self.down == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, self.left, self.right, self.up, "couch-clean"))

        #clean normal dirty spaces
        if self.pos == "l" and self.left == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, "clean", self.right, self.up, self.down))
        if self.pos == "r" and self.right == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, self.left, "clean", self.up, self.down))
        if self.pos == "u" and self.up == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, self.left, self.right, "clean", self.down))
        if self.pos == "d" and self.down == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, self.left, self.right, self.up, "clean"))
        return successors
    
    def is_goal(self):
        if (self.left == "clean" or self.left == "couch-clean") and (self.right == "clean" or self.right == "couch-clean") and (self.up == "clean" or self.up == "couch-clean") and (self.down == "clean" or self.down == "couch-clean"):
            return True
        else:
            return False
    
    def description(self):
        return "Simple vacuum cleaner agent for a 2x2 environment"
    
    def cost(self):
        return 1
    
    def env(self):
        return f'Action: {self.operator}\nVacuum cleaner position: {self.pos}\nUp:\n{self.up}, Left:\n{self.left}, Right:\n{self.right}, Down:\n{self.down}\nEtapa'


def main():
    print('\nIterative Deepening Depth-First Search: Simple Vacuum Cleaner 2x2 Agent that accounts for couches\n')
    state = AspiradorPo2x2Poltrona("start", "u", "couch-dirty", "dirty", "flipped-clean", "dirty")

    algorithm = BuscaLargura()
    start_time = time()

    print("\nSearching...")

    result = algorithm.search(state)
    end_time = time()

    if result != None:
        print('\nSolution found!')
        print(f"\nPath: {result.show_path()}")
        print(f"\nTime: {round(end_time-start_time, 3)} seconds")
    else:
        print('\nNo solution found.')

if __name__ == '__main__':
    main()