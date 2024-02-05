import pytest
from src.models.customer import Customer

def test_customer_initialization():
    # Setup
    customer_number = 1
    x_coord = 50
    y_coord = 60
    demand = 20
    ready_time = 10
    due_date = 100
    service_time = 5

    # Exercise
    customer = Customer(customer_number, x_coord, y_coord, demand, ready_time, due_date, service_time)

    # Verify
    assert customer.customer_number == customer_number
    assert customer.x_coord == x_coord
    assert customer.y_coord == y_coord
    assert customer.demand == demand
    assert customer.ready_time == ready_time
    assert customer.due_date == due_date
    assert customer.service_time == service_time

def test_customer_repr():
    # Setup
    customer = Customer(1, 50, 60, 20, 10, 100, 5)

    # Exercise
    repr_str = repr(customer)

    # Verify
    expected_repr = "Customer(1, Demand: 20, Due: 100)"
    assert repr_str == expected_repr
