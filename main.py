from src.utils import load_problem_instance
from src.models.problem_instance import ProblemInstance
from src.solvers import SolverFactory
from src.distance_matrix import DistanceMatrixSingleton

def main():
    file_path = 'data/C101test.json'
    customers, fleet = load_problem_instance(file_path)

    problem_instance = ProblemInstance(customers, fleet)

    DistanceMatrixSingleton(customers)
    distance_matrix = DistanceMatrixSingleton.get_distance_matrix()
    print("\nDistance Matrix: ")
    print(distance_matrix)

    solver_type = "insertion"  # Example: could be "insertion" or "random"
    solver = SolverFactory.get_solver(solver_type)

    solution = solver.solve(problem_instance)

    print("\nSolution Evaluation:")
    print(solution.evaluate())

if __name__ == "__main__":
    main()
