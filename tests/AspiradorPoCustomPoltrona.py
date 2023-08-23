from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State

class AspiradorPoCustomPoltrona(State):

    def __init__(self, op, pos, room):
        # You must use this name for the operator!
        self.operator = op
        self.pos = pos
        self.room = room
    
    def successors(self):
        successors = []
        successors.append(AspiradorPoCustomPoltrona("up", self.pos, self.room))
        # lalalaaalallalalalala
        return successors
    
    def is_goal(self):
        pass
    
    def description(self):
        return "Simple vacuum cleaner agent with adaptable environment size that accounts for couches"
    
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

    width = input("Enter the width of the environment: ")
    height = input("Enter the height of the environment: ")

    environment = []

    for i in range(int(height)):
        environment.append([])
        for j in range(int(width)):
            environment[i].append("clean")

    while True:
        print("Enter a room: coordinates (x, y), state (clean, dirty, couch-clean, couch-dirty, flipped-clean, flipped-dirty)")
        print("Example: 0 0 clean")
        print("Enter 'done' when finished")
        room = input()
        if room == "done":
            break
        else:
            room = room.split(" ")
            environment[int(room[1])].append(room[2])

    agentpos = input("Enter the agent's position: coordinates (x, y)")
    agentpos = agentpos.split(" ")
    agentpos = (int(agentpos[0]), int(agentpos[1]))
            

    print('\nIterative Deepening Depth-First Search: Simple Vacuum Cleaner Agent that accounts for couches\n')
    state = AspiradorPoCustomPoltrona("start", agentpos, room)
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Solution found!\n')
        print(f"Path: {result.show_path()}\n")
    else:
        print('No solution found.\n')

if __name__ == '__main__':
    main()