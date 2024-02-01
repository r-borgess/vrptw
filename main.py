from src.distance_matrix import DistanceMatrixSingleton

# Example customers list
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
