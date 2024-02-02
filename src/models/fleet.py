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
