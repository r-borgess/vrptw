from src.utils.general_utils import load_problem_instance
from src.models.problem_instance import ProblemInstance
from src.optimization.solvers import SolverFactory
from src.distance_matrix import DistanceMatrixSingleton
from src.view.plot import plot_routes

def main():
    # Load problem instance data
    file_path = 'data/C101.json'
    customers, fleet = load_problem_instance(file_path)

    # Initialize the problem instance
    problem_instance = ProblemInstance(customers, fleet)

    customer_locations = {customer.customer_number: (customer.x_coord, customer.y_coord) for customer in
                          problem_instance.customers}

    # Initialize or load your distance matrix
    DistanceMatrixSingleton(customers)  # Ensure this matches the singleton's method signature
    distance_matrix = DistanceMatrixSingleton.get_distance_matrix()

    # Instantiate the solver using the Solver Factory, adjust parameters as necessary
    solver = SolverFactory.get_solver("insertion", distance_matrix=distance_matrix, fleet=fleet)

    # Solve the problem
    solution = solver.solve(problem_instance)

    # Evaluate the solution
    evaluation_metrics = solver.evaluate_solution(solution, distance_matrix)

    # Print evaluation metrics
    print("Solution Evaluation:")
    for metric, value in evaluation_metrics.items():
        print(f"{metric}: {value}")

    # Call the visualization function
    plot_routes(solution, customer_locations, depot_location=customer_locations[0])

    # Output the solution
    print("Solution Routes:")
    for route in solution.routes:
        print(f"Route with total demand {route.total_demand} and distance {route.total_distance}:")
        for customer in route.customers:
            print(f"Customer {customer.customer_number}")

if __name__ == "__main__":
    main()
