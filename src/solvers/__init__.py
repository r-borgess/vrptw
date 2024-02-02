from .greedy_solver import GreedySolver
from .insertion_heuristic import InsertionHeuristic
from .random_solver import RandomSolver

class SolverFactory:
    @staticmethod
    def get_solver(solver_type, **kwargs):
        if solver_type == "greedy":
            return GreedySolver(**kwargs)
        elif solver_type == "insertion":
            return InsertionHeuristic(**kwargs)
        elif solver_type == "random":
            return RandomSolver(**kwargs)
        else:
            raise ValueError("Unknown solver type")
