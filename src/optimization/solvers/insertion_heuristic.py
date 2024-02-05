from src.models.problem_instance import ProblemInstance
from src.models.solution import Solution
from src.optimization.solvers.base_solver import BaseSolver
from src.models.route import Route


class InsertionHeuristic(BaseSolver):
    def __init__(self, distance_matrix, fleet):
        """
        Initialize the Insertion Heuristic solver with necessary parameters.

        :param distance_matrix: A 2D array or list representing distances between all pairs of locations.
        :param Fleet: A Fleet object representing fleet of vehicles available.
        """
        super().__init__()
        self.distance_matrix = distance_matrix
        self.fleet = fleet

    def solve(self, problem_instance: ProblemInstance) -> Solution:
        """
        Solves the VRPTW problem instance using the Insertion Heuristic.

        :param problem_instance: The VRPTW problem instance containing customers and their details.
        :return: A Solution object representing the optimized routes.
        """
        # Core solving logic, creating routes and inserting customers based on the heuristic.
        # Initialize a list of routes, one for each vehicle in the fleet
        routes = [Route(self.fleet.vehicle_capacity) for _ in range(self.fleet.total_vehicles)]

        # Copy of unassigned customers to work with
        unassigned_customers = problem_instance.customers.copy()

        # Flag to check if any customer was successfully inserted in the current iteration
        customer_inserted = True

        while unassigned_customers and customer_inserted:
            customer_inserted = False
            for customer in unassigned_customers[:]:  # Iterate over a copy of the list
                best_route, best_position, best_increase = self.find_best_insertion_for_customer(customer, routes)
                if best_route is not None:
                    # Insert the customer into the best route at the best position
                    best_route.add_customer(customer, best_position,self.distance_matrix)
                    unassigned_customers.remove(customer)
                    customer_inserted = True  # Mark successful insertion

        # Check if there are still unassigned customers
        if unassigned_customers:
            # Handle remaining unassigned customers, e.g., by logging, raising an error, or attempting re-optimization
            print(
                f"Warning: Unable to assign {len(unassigned_customers)} customers with the current fleet configuration.")

        # Compile the used routes into a Solution object (ignoring empty routes)
        solution_routes = [route for route in routes if route.customers]
        return Solution(solution_routes)

    def find_best_insertion_for_customer(self, customer, routes):
        """
        Determines the best route and position to insert a customer by evaluating
        the impact on route distance, capacity, and time windows.

        :param customer: The customer to be inserted.
        :param routes: A list of current routes.
        :return: A tuple containing the best route for insertion, the best position within that route,
                 and the associated minimal distance increase. If no feasible insertion is found,
                 returns (None, None, float('inf')).
        """
        best_route = None
        best_position = -1
        best_increase = float('inf')

        for route in routes:
            for position in range(len(route.customers) + 1):
                # Now passing distance_matrix to check_time_window_violation
                if not self.check_capacity_violation(route, customer):
                    increase = self.calculate_distance_increase(route, customer, position)

                    if increase < best_increase:
                        best_increase = increase
                        best_route = route
                        best_position = position

        return best_route, best_position, best_increase

    def calculate_distance_increase(self, route, customer, position):
        """
        Calculates the increase in distance for inserting a customer at a specified position within a route.

        :param route: The route being considered for customer insertion.
        :param customer: The customer to insert.
        :param position: The position in the route where the customer might be inserted.
        :return: The increase in total distance as a result of the insertion.
        """
        # Initialize distance increase to a large value if insertion is not feasible
        distance_increase = float('inf')

        # Calculate distance from the depot to the customer if inserting at the beginning
        if position == 0:
            if route.customers:
                next_customer = route.customers[0]
                distance_increase = self.distance_matrix[0][customer.customer_number] + \
                                    self.distance_matrix[customer.customer_number][next_customer.customer_number] - \
                                    self.distance_matrix[0][next_customer.customer_number]
            else:
                # If the route is empty, the increase is just the round trip to the customer
                distance_increase = 2 * self.distance_matrix[0][customer.customer_number]

        # Calculate distance for insertion at the end of the route
        elif position == len(route.customers):
            last_customer = route.customers[-1]
            distance_increase = self.distance_matrix[last_customer.customer_number][customer.customer_number] + \
                                self.distance_matrix[customer.customer_number][0] - \
                                self.distance_matrix[last_customer.customer_number][0]

        # Calculate distance for insertion between two customers
        else:
            prev_customer = route.customers[position - 1]
            next_customer = route.customers[position]
            distance_increase = self.distance_matrix[prev_customer.customer_number][customer.customer_number] + \
                                self.distance_matrix[customer.customer_number][next_customer.customer_number] - \
                                self.distance_matrix[prev_customer.customer_number][next_customer.customer_number]

        return distance_increase
