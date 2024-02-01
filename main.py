from src.distance_matrix import DistanceMatrixSingleton
from src.models import Customer, Route, Fleet

#Example customers list
customers = [
    {"customer_number": 0, "x_coord": 40.0, "y_coord": 50.0},
    {"customer_number": 1, "x_coord": 45.0, "y_coord": 68.0},
    # Add more customers as needed...
]

# Initialize the distance matrix
distance_matrix_singleton = DistanceMatrixSingleton(customers)

# Access the distance matrix
distance_matrix = distance_matrix_singleton.get_distance_matrix()

print(distance_matrix)

# Initialize the fleet with the total number of vehicles and their capacity
fleet = Fleet(total_vehicles=25, vehicle_capacity=200)

# During the solving process, when a new route is proposed:
proposed_route = Route(vehicle_capacity=fleet.vehicle_capacity)
# Assuming proposed_route is populated with customers...

if not fleet.is_capacity_exceeded(proposed_route) and fleet.add_route(proposed_route):
    print("Route successfully added to the fleet.")
else:
    print("Route cannot be added to the fleet due to capacity constraints.")
