import heapq

from .field import Cell, Field


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic_distance(a: Cell, b: Cell):
    (x1, y1) = a.x, a.y
    (x2, y2) = b.x, b.y
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(field: Field, start_cell: Cell, goal_cell: Cell):
    frontier = PriorityQueue()
    frontier.put(start_cell.coords_tuple(), 0)
    came_from = {}
    cost_so_far = {
        start_cell: 0
    }
    came_from[start_cell] = None

    while not frontier.is_empty():
        current = frontier.get()
        current_cell = field.get_cell_at_xy(*current)
        if current_cell == goal_cell:
            break

        for next_direction, next_cell in field.get_neighbor_cells(current_cell):
            if not next_cell.is_accessible:
                continue
            new_cost = cost_so_far[current_cell] + 1  # TODO: Add support for cost of movement
            if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                cost_so_far[next_cell] = new_cost
                priority = new_cost + heuristic_distance(next_cell, goal_cell)
                frontier.put(next_cell.coords_tuple(), priority)
                came_from[next_cell] = (current_cell, next_direction)

    return reconstruct_path(came_from, start_cell, goal_cell)


def reconstruct_path(came_from, start_cell, goal_cell):
    current = goal_cell
    path = []
    while current != start_cell:
        direction = came_from[current][1]
        path.append((current, direction))
        current = came_from[current][0]
    path.reverse()  # optional
    return path
