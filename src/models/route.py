class Route:
    def __init__(self, vehicle_capacity):
        self.customers = []  # List of customer objects
        self.total_demand = 0
        self.total_distance = 0  # Calculated using the distance matrix
        self.vehicle_capacity = vehicle_capacity  # Vehicle capacity

    def add_customer(self, customer, distance_matrix):
        # Check if adding this customer exceeds vehicle capacity
        if self.total_demand + customer.demand > self.vehicle_capacity:
            return False  # Cannot add this customer without exceeding capacity

        # Find the best position to insert this customer to minimize additional distance
        best_position = None
        best_increase = float('inf')
        for i in range(len(self.customers) + 1):
            # Calculate the increase in distance if the customer is inserted at position i
            increase = self.calculate_increase(customer, i, distance_matrix)
            if increase < best_increase:
                best_increase = increase
                best_position = i

        # Insert the customer into the best position
        self.customers.insert(best_position, customer)
        # Update total demand
        self.total_demand += customer.demand
        # Update total distance
        self.total_distance += best_increase
        return True

    def calculate_increase(self, customer, position, distance_matrix):
        # Calculate the increase in distance if the customer is inserted at the given position
        if position == 0:
            # Inserting at the beginning
            if self.customers:
                return distance_matrix[0][customer.customer_number] + distance_matrix[customer.customer_number][
                    self.customers[0].customer_number]
            else:
                return 2 * distance_matrix[0][customer.customer_number]  # Round trip to and from the depot
        elif position == len(self.customers):
            # Inserting at the end
            return distance_matrix[self.customers[-1].customer_number][customer.customer_number] + \
                distance_matrix[customer.customer_number][0] - distance_matrix[self.customers[-1].customer_number][0]
        else:
            # Inserting in the middle
            return distance_matrix[self.customers[position - 1].customer_number][customer.customer_number] + \
                distance_matrix[customer.customer_number][self.customers[position].customer_number] - \
                distance_matrix[self.customers[position - 1].customer_number][self.customers[position].customer_number]
