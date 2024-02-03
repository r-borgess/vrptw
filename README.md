
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

To update your README with information about the Solver Factory and extending the solver to include the new metaheuristic module, I'll draft sections that incorporate these updates. These revisions aim to reflect the enhanced capabilities of your project, emphasizing how users can leverage the Solver Factory for dynamic solver selection, including the use of metaheuristics for solution optimization.

### The Solver Factory

It is designed to dynamically instantiate solvers based on the specified solving strategy. With the recent introduction of the metaheuristic module, the factory now also supports the combination of constructive heuristics with advanced metaheuristic optimization techniques. This enhancement allows for a more versatile approach to solving the VRPTW, enabling users to not only generate initial solutions using heuristics like Greedy, Insertion, or Random algorithms but also refine these solutions with metaheuristics such as Tabu Search, Genetic Algorithm, and GRASP.

To use the Solver Factory, specify the desired solver type and, optionally, a metaheuristic for solution refinement. The factory will return a solver instance configured according to these specifications. For example:

```python
from src.solvers import SolverFactory

# Instantiate a solver with Tabu Search optimization
solver = SolverFactory.get_solver(solver_type="insertion", metaheuristic="tabu_search", **kwargs)
```

### Extending the Factory

Extending the VRPTW solvers list to incorporate new solving strategies or optimization techniques is straightforward, thanks to the modular design of the project. To add a new solver or metaheuristic:

1. **Adding a New Solver**:
   - Implement the new solver in the `src/solvers/` directory.
   - Ensure it extends the `BaseSolver` class and implements the `solve` method.
   - Register the new solver in the `SolverFactory` by adding a corresponding condition to the `get_solver` method.

2. **Adding a New Metaheuristic**:
   - Implement the metaheuristic in the `src/metaheuristics/` directory.
   - If applicable, extend the `MetaheuristicSolver` base class to leverage common functionalities.
   - Integrate the metaheuristic with the Solver Factory by updating the `combine_with_metaheuristic` method to recognize and correctly instantiate the new metaheuristic.

Example of adding a new metaheuristic:

```python
# Inside src/metaheuristics/new_metaheuristic.py
from .metaheuristic_solver import MetaheuristicSolver

class NewMetaheuristic(MetaheuristicSolver):
    def optimize(self, initial_solution, problem_instance):
        # Implementation of the optimization process
        pass
```

Then, update the `SolverFactory` to handle the new metaheuristic:

```python
# Modification in src/solvers/__init__.py within the SolverFactory

elif metaheuristic_type == "new_metaheuristic":
    return NewMetaheuristicOptimizer(base_solver, **kwargs)
```

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
