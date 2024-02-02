from src.solvers.greedy_solver import GreedySolver
from src.solvers.insertion_heuristic import InsertionHeuristic
from src.solvers.random_solver import RandomSolver


class SolverFactory:
    _solvers = {
        "greedy": GreedySolver,
        "insertion": InsertionHeuristic,
        "random": RandomSolver
    }

    @staticmethod
    def get_solver(solver_type):
        try:
            return SolverFactory._solvers[solver_type]()
        except KeyError:
            raise ValueError(f"Unknown solver type: {solver_type}")

