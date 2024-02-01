from src.utils import load_problem_instance
from src.distance_matrix import DistanceMatrixSingleton


def main():
    file_path = 'data/C101test.json'  # Ensure this path is correct
    customers, fleet = load_problem_instance(file_path)

    print("Loaded Customers:")
    for customer in customers:
        print(customer)

    DistanceMatrixSingleton(customers)
    distance_matrix = DistanceMatrixSingleton.get_distance_matrix()
    print("\nDistance Matrix: ")
    print(distance_matrix)

if __name__ == "__main__":
    main()
