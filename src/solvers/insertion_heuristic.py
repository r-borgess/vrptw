from src.models.problem_instance import ProblemInstance
from src.models.solution import Solution
from src.solvers.base_solver import BaseSolver
from src.models.route import Route
from src.models.customer import Customer


class InsertionHeuristic(BaseSolver):
    def __init__(self, distance_matrix, alpha1=1, alpha2=1, mu=1, lambda_weight=1, vehicle_capacity=100):
        super().__init__()  # Ensure to call the superclass initializer if needed
        self.distance_matrix = distance_matrix
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.mu = mu
        self.lambda_weight = lambda_weight
        self.vehicle_capacity = vehicle_capacity

    def solve(self, problem_instance: ProblemInstance) -> Solution:
        routes = []
        unassigned_customers = problem_instance.customers.copy()

        while unassigned_customers:
            inserted = False
            for customer in unassigned_customers:
                best_route, best_position, best_increase = None, None, float('inf')
                for route in routes:
                    for position in range(len(route.customers) + 1):
                        increase = route.calculate_increase(customer, position, self.distance_matrix)
                        if increase < best_increase and route.total_demand + customer.demand <= self.vehicle_capacity:
                            best_route, best_position, best_increase = route, position, increase

                # If a suitable position is found, insert the customer
                if best_route is not None:
                    best_route.add_customer(customer, self.distance_matrix)
                    unassigned_customers.remove(customer)
                    inserted = True
                    break  # Start looking for the next customer to insert

            # If no customers were inserted in this iteration, try creating a new route if possible
            if not inserted:
                if unassigned_customers:
                    new_route = Route(self.vehicle_capacity)
                    if new_route.add_customer(unassigned_customers[0], self.distance_matrix):
                        routes.append(new_route)
                        unassigned_customers.remove(unassigned_customers[0])
                else:
                    break  # No more customers to assign

        # Compile the routes into a Solution object
        return Solution(routes)

    def evaluate_solution(self, solution):
        """
        Evaluate the given solution, primarily based on the total distance of all routes.

        :param solution: Solution object containing all routes to evaluate.
        :return: The total distance of all routes in the solution.
        """
        total_distance = sum(route.total_distance for route in solution.routes)
        print(f"Total distance of the solution: {total_distance}")
        return total_distance