from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State

class AspiradorPo2x1(State):

    def __init__(self, op, pos, leftstate, rightstate):
        # You must use this name for the operator!
        self.operator = op
        self.pos = pos
        self.leftstate = leftstate
        self.rightstate = rightstate
    
    def successors(self):
        successors = []
        successors.append(AspiradorPo2x1("left", "l", self.leftstate, self.rightstate))
        successors.append(AspiradorPo2x1("right", "r", self.leftstate, self.rightstate))
        if self.pos == "l" and self.leftstate == "dirty":
            successors.append(AspiradorPo2x1("clean", self.pos, "clean", self.rightstate))
        if self.pos == "r" and self.rightstate == "dirty":
            successors.append(AspiradorPo2x1("clean", self.pos, self.leftstate, "clean"))
        return successors
    
    def is_goal(self):
        if self.leftstate == "clean" and self.rightstate == "clean":
            return True
        else:
            return False
    
    def description(self):
        return "Simple vacuum cleaner agent for a 2x1 environment"
    
    def cost(self):
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None


def main():
    print('\nIterative Deepening Depth-First Search: Simple Vacuum Cleaner 2x1 Agent\n')
    state = AspiradorPo2x1("start", "r", "dirty", "clean")
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Solution found!\n')
        print(f"Path: {result.show_path()}\n")
    else:
        print('No solution found.\n')

if __name__ == '__main__':
    main()