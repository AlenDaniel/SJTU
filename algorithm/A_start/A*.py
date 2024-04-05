# Example usage:
from srccode import a_star_search, Node
# Define a simple grid with 'S' as start, 'G' as goal, and '#' as obstacles
grid = [
    ['S', ' ', ' ', '#', ' '],
    [' ', ' ', '#', ' ', ' '],
    [' ', '#', ' ', ' ', ' '],
    [' ', ' ', ' ', 'G', ' ']
]

start_node = Node(0, 0)
goal_node = Node(3, 3)

path = a_star_search(
    start_node,
    goal_node,
    [[Node(x, y) for y in range(len(grid[0]))] for x in range(len(grid))],
    {(x, y) for x, row in enumerate(grid) for y, cell in enumerate(row) if cell == '#'}
)
if path:
    print(f"Found path: {path}")
else:
    print("No path found.")