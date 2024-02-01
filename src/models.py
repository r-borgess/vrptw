class Customer:
    def __init__(self, customer_number, x_coord, y_coord, demand, ready_time, due_date, service_time):
        self.customer_number = customer_number
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.demand = demand
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_time = service_time

class Fleet:
    def __init__(self, total_vehicles, vehicle_capacity):
        self.total_vehicles = total_vehicles
        self.vehicle_capacity = vehicle_capacity
        self.routes = []

    def add_route(self, route):
        if len(self.routes) < self.total_vehicles:
            self.routes.append(route)
            return True
        return False  # Cannot add more routes than available vehicles

    def total_distance(self):
        return sum(route.total_distance for route in self.routes)

    def is_capacity_exceeded(self, route):
        return route.total_demand > self.vehicle_capacity

    # You can add more methods as needed for managing the fleet and evaluating solutions

class Route:
    def __init__(self, vehicle_capacity):
        self.customers = []  # List of customer numbers
        self.total_demand = 0
        self.total_distance = 0  # Calculated using the distance matrix
        self.vehicle_capacity = vehicle_capacity  # Vehicle capacity is managed here if not using Vehicle objects

    def add_customer(self, customer, distance_matrix):
        # Implementation for adding a customer to the route, updating total_demand, and recalculating total_distance
        pass