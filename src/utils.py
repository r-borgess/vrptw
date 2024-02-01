import json
from src.models import Customer, Fleet


def load_problem_instance(file_path):
    """Load a VRPTW problem instance from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)

    customers = [Customer(customer_number=c['customer_number'],
                          x_coord=c['x_coord'],
                          y_coord=c['y_coord'],
                          demand=c['demand'],
                          ready_time=c['ready_time'],
                          due_date=c['due_date'],
                          service_time=c['service_time']) for c in data['customers']]

    # Initialize the fleet with total vehicles and capacity
    fleet = Fleet(total_vehicles=data['vehicle_number'], vehicle_capacity=data['capacity'])

    return customers, fleet
