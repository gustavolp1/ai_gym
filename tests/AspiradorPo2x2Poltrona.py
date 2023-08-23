from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State

class AspiradorPo2x2Poltrona(State):

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
        successors.append(AspiradorPo2x2Poltrona("top-left", "tl", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        successors.append(AspiradorPo2x2Poltrona("top-right", "tr", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        successors.append(AspiradorPo2x2Poltrona("bottom-left", "bl", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        successors.append(AspiradorPo2x2Poltrona("bottom-right", "br", self.topleftstate, self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        
        if self.pos == "tl" and self.topleftstate == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, "flipped-dirty", self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        if self.pos == "tr" and self.toprightstate == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, self.topleftstate, "flipped-dirty", self.bottomleftstate, self.bottomrightstate))
        if self.pos == "bl" and self.bottomleftstate == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, self.topleftstate, self.toprightstate, "flipped-dirty", self.bottomrightstate))
        if self.pos == "br" and self.bottomrightstate == "couch-dirty":
            successors.append(AspiradorPo2x2Poltrona("flip", self.pos, self.topleftstate, self.toprightstate, self.bottomleftstate, "flipped-dirty"))

        if self.pos == "tl" and self.topleftstate == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, "flipped-clean", self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        if self.pos == "tr" and self.toprightstate == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, self.topleftstate, "flipped-clean", self.bottomleftstate, self.bottomrightstate))
        if self.pos == "bl" and self.bottomleftstate == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, self.topleftstate, self.toprightstate, "flipped-clean", self.bottomrightstate))
        if self.pos == "br" and self.bottomrightstate == "flipped-dirty":
            successors.append(AspiradorPo2x2Poltrona("clean-couch", self.pos, self.topleftstate, self.toprightstate, self.bottomleftstate, "flipped-clean"))

        if self.pos == "tl" and self.topleftstate == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, "couch-clean", self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        if self.pos == "tr" and self.toprightstate == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, self.topleftstate, "couch-clean", self.bottomleftstate, self.bottomrightstate))
        if self.pos == "bl" and self.bottomleftstate == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, self.topleftstate, self.toprightstate, "couch-clean", self.bottomrightstate))
        if self.pos == "br" and self.bottomrightstate == "flipped-clean":
            successors.append(AspiradorPo2x2Poltrona("unflip", self.pos, self.topleftstate, self.toprightstate, self.bottomleftstate, "couch-clean"))

        if self.pos == "tl" and self.topleftstate == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, "clean", self.toprightstate, self.bottomleftstate, self.bottomrightstate))
        if self.pos == "tr" and self.toprightstate == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, self.topleftstate, "clean", self.bottomleftstate, self.bottomrightstate))
        if self.pos == "bl" and self.bottomleftstate == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, self.topleftstate, self.toprightstate, "clean", self.bottomrightstate))
        if self.pos == "br" and self.bottomrightstate == "dirty":
            successors.append(AspiradorPo2x2Poltrona("clean", self.pos, self.topleftstate, self.toprightstate, self.bottomleftstate, "clean"))
        return successors
    
    def is_goal(self):
        if (self.topleftstate == "clean" or self.topleftstate == "couch-clean") and (self.toprightstate == "clean" or self.toprightstate == "couch-clean") and (self.bottomleftstate == "clean" or self.bottomleftstate == "couch-clean") and (self.bottomrightstate == "clean" or self.bottomrightstate == "couch-clean"):
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
    print('\nIterative Deepening Depth-First Search: Simple Vacuum Cleaner 2x2 Agent that accounts for couches\n')
    state = AspiradorPo2x2Poltrona("start", "tr", "couch-dirty", "dirty", "flipped-clean", "dirty")
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Solution found!\n')
        print(f"Path: {result.show_path()}\n")
    else:
        print('No solution found.\n')

if __name__ == '__main__':
    main()