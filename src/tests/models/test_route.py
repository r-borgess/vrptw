import pytest
from src.models.route import Route
from src.models.customer import Customer

@pytest.fixture
def sample_route():
    return Route(vehicle_capacity=100)

@pytest.fixture
def sample_customer():
    return Customer(customer_number=1, x_coord=0, y_coord=0, demand=10, ready_time=0, due_date=100, service_time=10)

@pytest.fixture
def distance_matrix():
    # Example matrix, adjust based on actual logic; assume depot is at index 0
    return [[0, 10], [10, 0]]  # Simple distance matrix for two locations

def test_route_initialization(sample_route):
    assert sample_route.vehicle_capacity == 100
    assert sample_route.total_demand == 0
    assert sample_route.total_distance == 0
    assert len(sample_route.customers) == 0

def test_add_customer_success(sample_route, sample_customer, distance_matrix):
    position = 0  # Adding at the start of the route
    assert sample_route.add_customer(sample_customer, position, distance_matrix) == True
    assert len(sample_route.customers) == 1
    assert sample_route.total_demand == sample_customer.demand
    # Assuming correct total_distance calculation based on your logic
    assert sample_route.total_distance == 20  # To and from the depot

def test_add_customer_failure(sample_route, sample_customer, distance_matrix):
    position = None  # Invalid position
    assert sample_route.add_customer(sample_customer, position, distance_matrix) == False
    assert len(sample_route.customers) == 0  # Customer should not be added

def test_recalculate_total_distance_empty_route(sample_route, distance_matrix):
    sample_route.recalculate_total_distance(distance_matrix)
    assert sample_route.total_distance == 0  # No customers in route

def test_recalculate_total_distance(sample_route, sample_customer, distance_matrix):
    sample_route.add_customer(sample_customer, 0, distance_matrix)
    # Add more customers as needed to test the recalculation logic thoroughly
    sample_route.recalculate_total_distance(distance_matrix)
    # Test the total_distance after recalculation with expected value
    assert sample_route.total_distance == 20  # Example value, adjust based on your logic