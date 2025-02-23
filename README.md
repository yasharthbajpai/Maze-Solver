
# Maze Solver Visualizer

An interactive maze-solving visualizer built with Python, showcasing the implementation of **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **A* Search Algorithm**. The project uses the `curses` library to provide a terminal-based graphical representation of the maze and the pathfinding process.

---

## Features

- **Interactive Visualization**: Watch as the algorithms explore the maze step-by-step.
- **Multiple Algorithms**:
  - **BFS (Breadth-First Search)**: Explores all possible paths layer by layer.
  - **DFS (Depth-First Search)**: Explores paths deeply before backtracking.
  - **A* (A-Star Search)**: Uses a priority queue to find the shortest path efficiently.
- **Customizable Mazes**: Modify the maze structure directly in the code.

---

## Prerequisites

Before running the project, ensure you have Python installed on your system. Additionally, install the required dependency:

```
pip install windows-curses
```

> Note: The `windows-curses` package is required only for Windows systems. On Linux and macOS, the `curses` library is included by default.

---

## How to Run

1. Clone this repository to your local machine:
   ```
   git clone 
   cd 
   ```

2. Choose the algorithm you want to visualize:
   - For BFS: Run `bfs_maze_solver.py`
   - For DFS: Run `dfs_maze_solver.py`
   - For A*: Run `astar_maze_solver.py`

3. Execute the desired file:
   ```
   python bfs_maze_solver.py
   ```
   Replace `bfs_maze_solver.py` with the appropriate file name for DFS or A*.

4. Observe the algorithm solving the maze step-by-step in your terminal.

---

## File Descriptions

- **`bfs_maze_solver.py`**: Implements Breadth-First Search (BFS) for solving the maze.
- **`dfs_maze_solver.py`**: Implements Depth-First Search (DFS) for solving the maze.
- **`astar_maze_solver.py`**: Implements A* Search Algorithm for solving the maze.

---

## Maze Structure

The maze is represented as a 2D list in each file. Symbols used:
- `#`: Wall (not passable)
- `O`: Starting point
- `X`: Ending point
- Space (` `): Open path

Example of a simple maze:
```
maze = [
    ["#", "O", "#", "#", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", " ", "#", "#"],
    ["#", " ", " ", " ", "X"],
    ["#", "#", "#", "#", "#"]
]
```

Feel free to modify this structure to create your own mazes!


---

## Contributing

Contributions are welcome! If you'd like to improve this project or add new features, feel free to fork this repository, make changes, and submit a pull request.

---

## License

This project is licensed under the [Creative Commons Zero v1.0 Universal](LICENSE).  
You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.

---

## Acknowledgments

Special thanks to:
- The Python community for their excellent resources.
- The creators of the `curses` library for enabling terminal-based visualizations.

---

Happy Coding! 🚀
