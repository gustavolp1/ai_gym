from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State

class AspiradorPo2x2(State):

    def __init__(self, op, pos, topleftstate, toprightstate, bottomleftstate, bottomrightstate):
        # You must use this name for the operator!
        self.operator = op
        self.pos = pos
        self.topleftstate = topleftstate
        self.toprightstate = toprightstate
        self.bottomleftstate = bottomleftstate
        self.bottomrightstate = bottomrightstate
    
    def successors(self):
        successors = []
        successors.append(AspiradorPo2x2("top-left", "tl", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        successors.append(AspiradorPo2x2("top-right", "tr", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        successors.append(AspiradorPo2x2("bottom-left", "bl", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        successors.append(AspiradorPo2x2("bottom-right", "br", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))

        if self.pos == "tl" and self.topleftstate == "dirty":
            successors.append(AspiradorPo2x2("clean", self.pos, "clean", self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        if self.pos == "tr" and self.toprightstate == "dirty":
            successors.append(AspiradorPo2x2("clean", self.pos, self.topleftstate, "clean", self.bottomleftstate, self.bottomrightstate))
        if self.pos == "bl" and self.bottomleftstate == "dirty":
            successors.append(AspiradorPo2x2("clean", self.pos, self.topleftstate, self.toprightstate, "clean", self.bottomrightstate))
        if self.pos == "br" and self.bottomrightstate == "dirty":
            successors.append(AspiradorPo2x2("clean", self.pos, self.topleftstate, self.toprightstate, self.bottomleftstate, "clean"))
        return successors
    
    def is_goal(self):
        if self.topleftstate == "clean" and self.toprightstate == "clean" and self.bottomleftstate == "clean" and self.bottomrightstate == "clean":
            return True
        else:
            return False
    
    def description(self):
        return "Simple vacuum cleaner agent for a 2x2 environment"
    
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
    print('\nIterative Deepening Depth-First Search: Simple Vacuum Cleaner 2x2 Agent\n')
    state = AspiradorPo2x2("start", "tr", "dirty", "dirty", "dirty", "dirty")
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Solution found!\n')
        print(f"Path: {result.show_path()}\n")
    else:
        print('No solution found.\n')

if __name__ == '__main__':
    main()