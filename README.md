
# VRPTW Solver

## Overview

This project provides a solution framework for the Vehicle Routing Problem with Time Windows (VRPTW) by Heuristic-based route construction and Metaheuristics refinement.

---

## Features
- **Insertion Heuristic**: A flexible and efficient strategy for route optimization, considering distance and time constraints.
- **Solver Factory**: Facilitates easy switching between different solving strategies, including the newly added Insertion Heuristic.
- **Enhanced Route Management**: The `Route` model supports dynamic customer insertion, automatically recalculating total demand and distance.

# VRPTW Solver

## Overview

This project provides a comprehensive solution framework for the Vehicle Routing Problem with Time Windows (VRPTW). It features a variety of solving strategies, including Greedy, Insertion Heuristic, and Random solvers, alongside a robust visualization module for plotting routes. Our approach allows for flexible problem solving and analysis, facilitating the exploration of different algorithms' effectiveness.

## Project Structure

```
vrptw_solver/
│
├── data/                          # Contains JSON-formatted problem instances.
│   └── instance.json              # Example problem instance file.
│
├── src/                           # Source code directory for all solver components.
│   ├── __init__.py                # Initializes the src package, allowing for relative imports.
│   ├── distance_matrix.py         # Manages distance matrix calculations essential for solving VRPTW.
│   ├── utils.py                   # Includes utility functions for data loading and other common tasks.
│   ├── view.py                    # Provides visualization capabilities for solutions using graphical plots.
│   │
│   ├── models/                    # Data models directory for representing entities such as customers and fleet.
│   │   ├── __init__.py            # Initializes the models package.
│   │   ├── customer.py            # Defines the Customer model with properties like demand and time windows.
│   │   ├── fleet.py               # Defines the Fleet model, including vehicle capacity and management methods.
│   │   ├── problem_instance.py    # Represents a VRPTW problem instance, linking customers and fleet.
│   │   ├── route.py               # Represents a single route, including the sequence of customers.
│   │   └── solution.py            # Represents a solution to a VRPTW instance, comprising multiple routes.
│   │
│   ├── solvers/                   # Solvers directory for different VRPTW solving algorithms.
│   │   ├── __init__.py            # Contains SolverFactory for dynamic solver instantiation based on type.
│   │   ├── base_solver.py         # Base class for solver implementations, defining the common solver interface.
│   │   ├── greedy_solver.py       # Greedy algorithm solver implementation.
│   │   ├── insertion_heuristic.py # Insertion heuristic solver for constructing initial solutions.
│   │   └── random_solver.py       # Random solver for benchmarking and testing.
│   │
│   └── metaheuristics/            # Metaheuristics directory for advanced solution optimization techniques.
│       ├── __init__.py            # Initializes the metaheuristics package.
│       ├── metaheuristic_solver.py # Base class for metaheuristic solvers, defining the common interface.
│       ├── tabu_search.py         # Tabu Search metaheuristic implementation.
│       ├── genetic_algorithm.py   # Genetic Algorithm metaheuristic implementation.
│       └── grasp.py               # GRASP (Greedy Randomized Adaptive Search Procedure) implementation.
│
└── main.py                        # Main executable script for running the VRPTW solver with various configurations.
```

## Solver Factory

The `SolverFactory` in `src/solvers/__init__.py` allows for easy selection among different solver strategies based on their names. Supported solvers are "greedy", "insertion", and "random". This flexibility enables quick comparisons and benchmarking across various algorithms.

## Extending the Solver

To add new solver algorithms, implement the solver class in `src/solvers/`, ensuring it inherits from `BaseSolver` and implements the required methods. Register the new solver in the `SolverFactory` for seamless integration.

---

## Setup

1. Ensure Python 3.8+ is installed on your system.
2. Install required Python packages:

```bash
pip install numpy plotly
```

3. Place your problem instance JSON files in the `data/` directory.

## Usage

You can specify the solver type dynamically via the `SolverFactory` interface.
To run the solver with a problem instance, execute the `main.py` script:

```bash
python main.py
```

This script will load the problem instance, calculate the distance matrix, run the solver, and plot the resulting routes.

## Visualization

The visualization module uses `plotly` to plot the routes generated by the solver. Each route is displayed with different markers and lines for easy differentiation.

## Contributing

Contributions to the VRPTW Solver project are welcome. Please follow the standard fork and pull request workflow.

## License

GNU General Public License v3.0
