import pytest
from src.models.fleet import Fleet
from src.models.route import Route

@pytest.fixture
def sample_fleet():
    return Fleet(total_vehicles=2, vehicle_capacity=100)

@pytest.fixture
def sample_route():
    return Route(vehicle_capacity=100)

def test_fleet_initialization(sample_fleet):
    assert sample_fleet.total_vehicles == 2
    assert sample_fleet.vehicle_capacity == 100
    assert len(sample_fleet.routes) == 0

def test_add_route_success(sample_fleet, sample_route):
    assert sample_fleet.add_route(sample_route) == True
    assert len(sample_fleet.routes) == 1

def test_add_route_failure(sample_fleet, sample_route):
    sample_fleet.add_route(sample_route)  # First route added
    sample_fleet.add_route(sample_route)  # Second route added
    assert sample_fleet.add_route(sample_route) == False  # Should fail as fleet is full
    assert len(sample_fleet.routes) == 2  # No additional route should be added

def test_total_distance(sample_fleet, sample_route):
    sample_fleet.add_route(sample_route)
    # Assuming adding the same route for simplicity; adjust based on actual Route model
    sample_fleet.add_route(sample_route)
    expected_distance = sample_route.total_distance * 2
    assert sample_fleet.total_distance() == expected_distance

def test_is_capacity_exceeded(sample_fleet, sample_route):
    assert not sample_fleet.is_capacity_exceeded(sample_route)  # Assuming vehicle_capacity > total_demand
    # To test capacity exceeded, either modify sample_route's total_demand or create a new route fixture
