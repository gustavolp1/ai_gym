from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State
from datetime import datetime

class TaxiDriver(State):

    def __init__(self, op, pos, goal, passenger_pos, map, picked_up):
        self.operator = op
        self.pos = pos
        self.goal = goal
        self.passenger_pos = passenger_pos
        self.map = map
        self.picked_up = picked_up

    def successors(self):
        successors = []
        if self.pos[1] > 0: 
            successors.append(TaxiDriver('move_up', (self.pos[0], self.pos[1] - 1), self.goal, self.passenger_pos, self.map, self.picked_up))
        if self.pos[1] < self.map[1]:
            successors.append(TaxiDriver('move_down', (self.pos[0], self.pos[1] + 1), self.goal, self.passenger_pos, self.map, self.picked_up))
        if self.pos[0] > 0:
            successors.append(TaxiDriver('move_left', (self.pos[0] - 1, self.pos[1]), self.goal, self.passenger_pos, self.map, self.picked_up))
        if self.pos[0] < self.map[0]:
            successors.append(TaxiDriver('move_right', (self.pos[0] + 1, self.pos[1]), self.goal, self.passenger_pos, self.map, self.picked_up))

        if self.pos == self.passenger_pos and self.picked_up == False:
            successors.append(TaxiDriver('pick_up', self.pos, self.goal, self.passenger_pos, self.map, True))

        return successors

    def is_goal(self):
        if self.pos == self.goal and self.picked_up == True:
            return True
        return False

    def description(self):
        return "Taxi Driver Problem with passenger and goal"

    def cost(self):
        if self.operator == 'pick_up':
            return 2
        return 1

    def env(self):
        return f'{self.operator} - {self.pos[0]} {self.pos[1]} - {self.picked_up}'
    
    def h(self):
        if self.picked_up == False:
            return ((self.pos[0] - self.passenger_pos[0])**2 + (self.pos[1] - self.passenger_pos[1])**2)**0.5
        else:
            return ((self.pos[0] - self.goal[0])**2 + (self.pos[1] - self.goal[1])**2)**0.5

def main():

    algorithm = AEstrela()

    state = TaxiDriver('Start', (0, 0), (0, 4), (5, 0), (6, 4), False)
    # dimensoes do mapa devem ser passadas menos 1, pois o mapa comeca em 0
    print('\nSearching...')

    start_time = datetime.now()
    result = algorithm.search(state, trace=True)
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