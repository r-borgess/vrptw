class Customer:
    def __init__(self, customer_number, x_coord, y_coord, demand, ready_time, due_date, service_time):
        self.customer_number = customer_number
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.demand = demand
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_time = service_time

    def __repr__(self):
        return f"Customer({self.customer_number}, Demand: {self.demand}, Due: {self.due_date})"
