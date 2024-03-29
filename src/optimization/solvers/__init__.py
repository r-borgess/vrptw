# Adjust the import paths based on your project structure
from src.optimization.solvers.greedy_solver import GreedySolver
from src.optimization.solvers.insertion_heuristic import InsertionHeuristic
from src.optimization.solvers.random_solver import RandomSolver
# Import metaheuristic classes
from src.optimization.metaheuristics.tabu_search import TabuSearch
from src.optimization.metaheuristics.genetic_algorithm import GeneticAlgorithm
from src.optimization.metaheuristics.grasp import GRASP

class SolverFactory:
    @staticmethod
    def get_solver(solver_type, metaheuristic_type=None, **kwargs):
        # Base solver selection
        solvers = {
            "greedy": GreedySolver,
            "insertion": InsertionHeuristic,
            "random": RandomSolver
        }

        if solver_type not in solvers:
            raise ValueError("Unknown solver type")

        base_solver = solvers[solver_type](**kwargs)

        # Metaheuristic enhancement
        if metaheuristic_type:
            metaheuristics = {
                "tabu_search": TabuSearch,
                "genetic_algorithm": GeneticAlgorithm,
                "grasp": GRASP
            }

            if metaheuristic_type not in metaheuristics:
                raise ValueError("Unknown metaheuristic type")

            # Enhance the base solver with the selected metaheuristic
            return metaheuristics[metaheuristic_type](base_solver, **kwargs)

        return base_solver
