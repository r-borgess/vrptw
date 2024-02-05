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

    def check_capacity_violation(self, route, customer):
        """
        Checks if adding a customer to the route exceeds the vehicle's capacity.

        :param route: The route to check.
        :param customer: The customer being considered for insertion.
        :return: True if insertion violates capacity, False otherwise.
        """
        return route.total_demand + customer.demand > route.vehicle_capacity

    def check_time_window_violation(self, route, customer, position, distance_matrix):
        """
        Checks if inserting the customer at the specified position causes any time window violations
        for the customer or subsequent customers in the route.

        :param route: The route to check.
        :param customer: The customer being considered for insertion.
        :param position: The position at which the customer would be inserted.
        :param distance_matrix: The distance matrix used for distance calculations.
        :return: True if insertion causes time window violations, False otherwise.
        """
        # Assume service time at depot starts at time 0
        current_time = 0

        # Calculate the arrival time at each customer in the route after the potential insertion
        for i, route_customer in enumerate(route.customers):
            if i == position:
                # Calculate time to arrive at the new customer
                prev_customer = route.customers[i - 1] if i > 0 else None
                to_new_customer = distance_matrix[prev_customer.customer_number][
                    customer.customer_number] if prev_customer else distance_matrix[0][customer.customer_number]
                current_time += to_new_customer

                # Check time window for the inserted customer
                if not (customer.ready_time <= current_time <= customer.due_date):
                    return True  # Violation found

                # Add service time of the inserted customer
                current_time += customer.service_time

            # Calculate time to next customer (or to the new customer if it's the first iteration after insertion)
            next_customer = customer if i == position else route_customer
            travel_time = distance_matrix[route.customers[i - 1].customer_number][
                next_customer.customer_number] if i > 0 else distance_matrix[0][next_customer.customer_number]
            current_time += travel_time

            # Check the time window of the next customer
            if current_time < next_customer.ready_time:
                current_time = next_customer.ready_time  # Wait for the time window to open
            if current_time > next_customer.due_date:
                return True  # Violation found

            # Add service time of the next customer
            current_time += next_customer.service_time

        # Check the last customer if the new customer is appended at the end
        if position == len(route.customers):
            travel_time = distance_matrix[route.customers[-1].customer_number][
                customer.customer_number] if route.customers else distance_matrix[0][customer.customer_number]
            current_time += travel_time
            if not (customer.ready_time <= current_time <= customer.due_date):
                return True  # Violation found

        # No violations found
        return False

    def calculate_arrival_time(self, route, customer_index, distance_matrix):
        """
        Calculates the arrival time at a specific customer in a route, considering travel and customer service times.

        :param route: The route containing the sequence of customer visits.
        :param customer_index: The index of the customer in the route for whom to calculate the arrival time.
        :param distance_matrix: A 2D array containing the travel times/distances between all pairs of locations.
        :return: The arrival time at the specified customer.
        """
        arrival_time = 0  # Assuming the depot/vehicle starts at time 0

        for i in range(customer_index + 1):  # Adjust loop to include target customer
            if i == 0:
                # From depot to the first customer
                arrival_time += distance_matrix[0][route.customers[0].customer_number]
            else:
                # From previous customer to the current one
                arrival_time += distance_matrix[route.customers[i - 1].customer_number][
                    route.customers[i].customer_number]

            # Add service time at the current customer (if not calculating for the first customer)
            if i > 0:
                arrival_time += route.customers[i - 1].service_time

        return arrival_time

    def evaluate_solution(self, solution, distance_matrix):
        """
        Evaluates the solution based on total distance, the number of time window violations, and the number of routes used.

        :param solution: The solution object containing all routes to evaluate.
        :param distance_matrix: The distance matrix used for calculating travel times.
        :return: A dictionary with evaluation metrics including total distance, time window violations, and number of vehicles used.
        """
        total_distance = 0
        time_window_violations = 0
        number_of_vehicles_used = len(solution.routes)

        for route in solution.routes:
            total_distance += route.total_distance
            for idx, customer in enumerate(route.customers):
                arrival_time = self.calculate_arrival_time(route, idx, distance_matrix)
                if not (customer.ready_time <= arrival_time <= customer.due_date):
                    time_window_violations += 1

        evaluation_metrics = {
            'total_distance': total_distance,
            'time_window_violations': time_window_violations,
            'number_of_vehicles_used': number_of_vehicles_used
        }

        return evaluation_metrics
