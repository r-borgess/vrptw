import plotly.graph_objects as go


def plot_routes(solution, customer_locations, depot_location=(0, 0)):
    """
    Visualizes the routes using Plotly.

    :param solution: A Solution object containing all the routes.
    :param customer_locations: A dictionary with customer numbers as keys and (x, y) coordinates as values.
    :param depot_location: A tuple representing the (x, y) coordinates of the depot.
    """
    fig = go.Figure()

    # Plot each route with a different color
    for route in solution.routes:
        # Start and end at the depot
        route_coords = [depot_location] + [customer_locations[customer.customer_number] for customer in
                                           route.customers] + [depot_location]
        xs, ys = zip(*route_coords)

        # Add route line
        fig.add_trace(go.Scatter(x=xs, y=ys, mode='lines+markers', name='Route'))

    # Highlight the depot location
    fig.add_trace(
        go.Scatter(x=[depot_location[0]], y=[depot_location[1]], mode='markers', marker=dict(size=10, color='red'),
                   name='Depot'))

    # Customize layout
    fig.update_layout(title='VRPTW Routes Visualization', xaxis_title='X Coordinate', yaxis_title='Y Coordinate',
                      showlegend=False)

    fig.show()
