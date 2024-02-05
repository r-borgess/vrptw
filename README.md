# vrptw

## Overview

This project provides a solution framework for the Vehicle Routing Problem with Time Windows (VRPTW) by heuristic-based route construction and metaheuristics refinement.

---

## Features

- **Heuristic route construction**: A flexible and efficient strategy for creating route initialization algorithms, considering distance and time constraints.
- **Metaheuristic refinement**: A flexible and efficient strategy for creating solution refinement algorithms, now including a dedicated `optimization` directory for solvers and metaheuristics.
- **Solver Factory**: Facilitates easy switching between different solving strategies.
- **Problem Modeling**: Facilitates the definition of different types of problems.
- **Visualization Module**: Enhanced plotting of the obtained solutions in a web-based graph, now organized within a `view` subdirectory for improved modularity and potential future expansion.
- **Utility Functions**: A new `utils` subdirectory housing general utilities (`general_utils.py`) and move-related functionalities (`moves.py`), supporting various aspects of the solution process.

---

## Project Structure

```
vrptw_solver/
│
├── src/
│   ├── models/                    # Data models like Customer, Fleet, etc.
│   ├── optimization/              # Contains both solvers and metaheuristics.
│   │   ├── metaheuristics/        # Advanced optimization techniques.
│   │   └── solvers/               # Initial solution generation strategies.
│   ├── utils/                     # Utility functions supporting the project.
│   │   ├── general_utils.py       # General-purpose utilities.
│   │   └── moves.py               # Utilities for move operations.
│   └── view/                      # Visualization capabilities.
│       └── plot.py                # Plotting solutions using `plotly`.
├── tests/                         # Test suite for the project.
│   ├── models/                    # Tests for the data models.
│   ├── optimization/              # Tests for solvers and metaheuristics.
│   ├── utils/                     # Tests for utility functions.
│   └── view/                      # Tests for visualization functionalities.
└── main.py                        # Main executable script.
```

## Setup

1. Ensure Python 3.8+ is installed on your system.
2. Install required Python packages:

```bash
pip install numpy plotly pytest
```

3. Place your problem instance JSON files in the appropriate directory.

## Testing

To ensure the reliability of the VRPTW solver, comprehensive tests have been provided in the `tests` directory. Run the tests using the following command:

```bash
pytest
```

This command will automatically discover and execute all test cases, helping to maintain the integrity of the solution framework.

## Usage

Run the solver with a problem instance by executing the `main.py` script:

```bash
python main.py
```

This script will load the problem instance, calculate the distance matrix, run the solver based on the specified configuration, and plot the resulting routes.

## Contributing

Contributions are welcome! Please follow the standard fork and pull request workflow. Do not forget to add tests for new features or bug fixes.

## License

GNU General Public License v3.0
---

This updated README includes the latest project structure, emphasizes the new `utils` and `view` subdirectories, and introduces instructions for running tests with pytest. Adjust the content as necessary to fit your project's specifics, especially the details under "Setup" and "Usage" if there are specific requirements or steps I might not be aware of.
