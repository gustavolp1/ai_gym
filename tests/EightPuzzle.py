from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State
from datetime import datetime

class EightPuzzle(State):

    def __init__(self, op, pos, goal, map):
        self.operator = op
        self.pos = pos
        self.goal = goal
        self.map = map

    def successors(self):
        successors = []
        
        if self.pos[1] > 0:
            map_2 = self.map.copy()
            map_2[self.pos[0]][self.pos[1]], map_2[self.pos[0]][self.pos[1] - 1] = map_2[self.pos[0]][self.pos[1] - 1], map_2[self.pos[0]][self.pos[1]]
            successors.append(EightPuzzle('move_up', (self.pos[0], self.pos[1] - 1), self.goal, map_2))
        if self.pos[1] < 2:
            map_2 = self.map.copy()
            map_2[self.pos[0]][self.pos[1]], map_2[self.pos[0]][self.pos[1] + 1] = map_2[self.pos[0]][self.pos[1] + 1], map_2[self.pos[0]][self.pos[1]]
            successors.append(EightPuzzle('move_down', (self.pos[0], self.pos[1] + 1), self.goal, map_2))
        if self.pos[0] > 0:
            map_2 = self.map.copy()
            map_2[self.pos[0]][self.pos[1]], map_2[self.pos[0] - 1][self.pos[1]] = map_2[self.pos[0] - 1][self.pos[1]], map_2[self.pos[0]][self.pos[1]]
            successors.append(EightPuzzle('move_left', (self.pos[0] - 1, self.pos[1]), self.goal, map_2))
        if self.pos[0] < 2:
            map_2 = self.map.copy()
            map_2[self.pos[0]][self.pos[1]], map_2[self.pos[0] + 1][self.pos[1]] = map_2[self.pos[0] + 1][self.pos[1]], map_2[self.pos[0]][self.pos[1]]
            successors.append(EightPuzzle('move_right', (self.pos[0] + 1, self.pos[1]), self.goal, map_2))

        return successors

    def is_goal(self):
        if self.map == self.goal:
            return True
        return False

    def description(self):
        return "8-Puzzle Problem"

    def cost(self):
        return 1

    def env(self):
        return f'{self.operator} - {self.pos[0]} {self.pos[1]}'
    
    def h(self):
    # manhattan distance
        total_distance = 0
        for i in range(3):
            for j in range(3):
                value = self.map[i][j]
                if value != 0:
                    goal_position = None
                    for row in self.goal:
                        if value in row:
                            goal_position = (self.goal.index(row), row.index(value))
                            break
                    total_distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        return total_distance



def main():

    eight_table = [[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 0]]
    
    loop_table = [[1, 2, 3], 
                   [8, 0, 4], 
                   [7, 6, 5]]
    
    input_table =  [[1, 8, 2],
                    [0, 4, 3],
                    [7, 6, 5]]

    algorithm = AEstrela()

    state = EightPuzzle('Start', (2, 1), eight_table, input_table)
    
    print('\nSearching...')

    start_time = datetime.now()
    result = algorithm.search(state)
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