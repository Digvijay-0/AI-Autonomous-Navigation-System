import heapq

class AStarPlanner:
    def __init__(self, grid):
        self.grid = grid
        self.rows, self.cols = grid.shape

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (0, start))
        came_from = {}
        cost = {start: 0}

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == goal:
                break

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)

                if 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.cols:
                    if self.grid[neighbor] == 1:
                        continue

                    new_cost = cost[current] + 1
                    if neighbor not in cost or new_cost < cost[neighbor]:
                        cost[neighbor] = new_cost
                        priority = new_cost + self.heuristic(goal, neighbor)
                        heapq.heappush(open_list, (priority, neighbor))
                        came_from[neighbor] = current

        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from.get(current, start)
        path.append(start)
        path.reverse()

        return path