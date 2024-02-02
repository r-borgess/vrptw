from src.utils import load_problem_instance
from src.models.problem_instance import ProblemInstance
from src.solvers import SolverFactory
from src.distance_matrix import DistanceMatrixSingleton

def main():
    # Load problem instance data
    file_path = 'data/C101.json'
    customers, fleet = load_problem_instance(file_path)

    # Initialize the problem instance
    problem_instance = ProblemInstance(customers, fleet)

    # Initialize or load your distance matrix
    DistanceMatrixSingleton(customers)
    distance_matrix = DistanceMatrixSingleton.get_distance_matrix()

    # Select the solver type dynamically, e.g., based on user input or configuration
    solver_type = "insertion"  # This could be parameterized as needed

    # Instantiate the solver using the Solver Factory
    solver = SolverFactory.get_solver(solver_type, distance_matrix=distance_matrix, vehicle_capacity=fleet.vehicle_capacity)

    # Solve the problem
    solution = solver.solve(problem_instance)

    # Output the solution
    print("Solution Routes:")
    for route in solution.routes:
        print(f"Route with total demand {route.total_demand} and distance {route.total_distance}:")
        for customer in route.customers:
            print(f"Customer {customer.customer_number}")

if __name__ == "__main__":
    main()
