import pytest
from src.models.problem_instance import ProblemInstance
from src.models.customer import Customer
from src.models.fleet import Fleet


@pytest.fixture
def sample_customers():
    # Create a list of sample Customer objects
    return [Customer(customer_number=i, x_coord=0, y_coord=0, demand=10, ready_time=0, due_date=10, service_time=0) for
            i in range(1, 6)]


@pytest.fixture
def sample_fleet():
    # Create a sample Fleet object
    return Fleet(total_vehicles=2, vehicle_capacity=100)


def test_problem_instance_initialization(sample_customers, sample_fleet):
    problem_instance = ProblemInstance(customers=sample_customers, fleet=sample_fleet)

    assert len(problem_instance.customers) == 5  # Assuming 5 sample customers were created
    assert isinstance(problem_instance.customers[0], Customer)
    assert isinstance(problem_instance.fleet, Fleet)
    assert problem_instance.fleet.total_vehicles == 2
    # Can also assert the integrity of the fleet's vehicle capacity or any other attributes