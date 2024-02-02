class Route:
    def __init__(self, vehicle_capacity):
        self.customers = []  # List of customer numbers
        self.total_demand = 0
        self.total_distance = 0  # Calculated using the distance matrix
        self.vehicle_capacity = vehicle_capacity  # Vehicle capacity is managed here if not using Vehicle objects

    def add_customer(self, customer, distance_matrix):
        # Implementation for adding a customer to the route, updating total_demand, and recalculating total_distance
        pass