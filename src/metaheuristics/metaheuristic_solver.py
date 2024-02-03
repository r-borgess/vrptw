from abc import ABC, abstractmethod
from src.models.solution import Solution
from src.models.problem_instance import ProblemInstance

class MetaheuristicSolver(ABC):
    def __init__(self, problem_instance: ProblemInstance, initial_solution: Solution):
        """
        Initialize the metaheuristic solver with a problem instance and an initial solution.

        Parameters:
            problem_instance (ProblemInstance): The VRPTW problem instance to be optimized.
            initial_solution (Solution): An initial solution to the problem instance, typically obtained from a constructive heuristic.
        """
        self.problem_instance = problem_instance
        self.current_solution = initial_solution
        self.best_solution = initial_solution  # Keeps track of the best solution found during the search

    @abstractmethod
    def optimize(self):
        """
        Performs the optimization process, refining the initial solution using the metaheuristic approach.

        Should update self.best_solution with the best found solution.
        """
        pass

    def evaluate_solution(self, solution: Solution) -> float:
        """
        Evaluates a given solution, returning a score or cost associated with it.
        This could wrap the existing evaluate_solution method in BaseSolver or implement specific evaluation logic.

        Parameters:
            solution (Solution): The solution to evaluate.

        Returns:
            float: The evaluation score or cost of the solution.
        """
        # Placeholder for evaluation logic; actual implementation may vary
        return solution.evaluate()

    def update_solution(self, new_solution: Solution):
        """
        Updates the current and best solutions if the new solution is better.

        Parameters:
            new_solution (Solution): The new solution to consider.
        """
        # Placeholder for the logic to update the current and best solutions
        pass

    def generate_neighbors(self, solution: Solution) -> [Solution]:
        """
        Generates a list of neighboring solutions to the given solution.

        Parameters:
            solution (Solution): The solution for which to find neighbors.

        Returns:
            [Solution]: A list of neighboring solutions.
        """
        # Placeholder for neighbor generation logic; actual implementation may vary
        return []

    # Additional methods as needed for specific metaheuristic operations, e.g., managing tabu lists in Tabu Search
