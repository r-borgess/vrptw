from abc import ABC, abstractmethod


class BaseSolver(ABC):

    @abstractmethod
    def solve(self, problem_instance):
        """
        Solve the VRPTW problem instance.

        Parameters:
            problem_instance (ProblemInstance): An instance of the problem to be solved.

        Returns:
            Solution: An optimized solution for the problem instance.
        """
        pass

    @abstractmethod
    def evaluate_solution(self, solution):
        """
        Evaluate the given solution.

        Parameters:
            solution (Solution): The solution to evaluate.

        Returns:
            float: The cost or score of the solution.
        """
        pass
