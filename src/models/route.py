class Route:
    def __init__(self, vehicle_capacity):
        self.customers = []  # List of customer objects
        self.total_demand = 0
        self.total_distance = 0  # Calculated using the distance matrix
        self.vehicle_capacity = vehicle_capacity  # Vehicle capacity

    def add_customer(self, customer, position, distance_matrix):
        """Inserts a customer into the route at the specified position."""
        # Simplified to assume position is already determined as optimal
        if position is not None:
            # Update route with new customer
            self.customers.insert(position, customer)
            self.total_demand += customer.demand
            # Recalculate total distance since it might change with the new customer
            self.recalculate_total_distance(distance_matrix)
            return True
        return False

    def recalculate_total_distance(self, distance_matrix):
        """
        Recalculates the total distance of the route based on the current sequence of customers.
        Includes the distance from/to the depot to the first/last customer.

        :param distance_matrix: A 2D list or array where distance_matrix[i][j] represents
                                the distance between customer i and customer j, with 0 being the depot.
        """
        if not self.customers:
            self.total_distance = 0
            return

        # Reset total_distance before recalculation
        self.total_distance = 0

        # Distance from the depot to the first customer and from the last customer back to the depot
        self.total_distance += distance_matrix[0][self.customers[0].customer_number]
        self.total_distance += distance_matrix[self.customers[-1].customer_number][0]
