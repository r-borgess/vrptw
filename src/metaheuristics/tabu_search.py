from src.models.solution import Solution
from src.models.problem_instance import ProblemInstance
from .metaheuristic_solver import MetaheuristicSolver

class Move:
    def __init__(self, customer_a, customer_b, route_a, route_b):
        self.customer_a = customer_a
        self.customer_b = customer_b
        self.route_a = route_a
        self.route_b = route_b

    def __hash__(self):
        return hash((self.customer_a.customer_number, self.customer_b.customer_number, self.route_a, self.route_b))

    def __eq__(self, other):
        return (self.customer_a.customer_number == other.customer_a.customer_number and
                self.customer_b.customer_number == other.customer_b.customer_number and
                self.route_a == other.route_a and
                self.route_b == other.route_b)

class TabuSearch(MetaheuristicSolver):
    def __init__(self, problem_instance: ProblemInstance, initial_solution: Solution, tabu_size, tenure, max_iterations_without_improvement):
        super().__init__(problem_instance, initial_solution)
        self.tabu_list = set()  # Use a set for efficient lookups
        self.tabu_tenures = {}  # Maps moves to their remaining tabu tenure
        self.tabu_size = tabu_size
        self.tenure = tenure
        self.max_iterations_without_improvement = max_iterations_without_improvement
        self.iterations_without_improvement = 0

    def optimize(self):
        while self.iterations_without_improvement < self.max_iterations_without_improvement:
            neighbors = self.generate_neighbors(self.current_solution)
            best_neighbor, best_move = None, None
            best_score = float('inf')
            for neighbor, move in neighbors:
                if move in self.tabu_list and not self.aspiration_criteria_met(neighbor):
                    continue
                score = self.evaluate_solution(neighbor)
                if score < best_score:
                    best_neighbor, best_move, best_score = neighbor, move, score
            if best_neighbor:
                self.update_solution(best_neighbor)
                self.update_tabu_list(best_move)
            else:
                self.iterations_without_improvement += 1

    def generate_neighbors(self, solution: Solution) -> [(Solution, Move)]:
        # Implementation to generate neighboring solutions by swapping customers
        # Return both the neighbor solution and the move made to achieve it
        neighbors = []
        # Example logic to generate swap moves (to be implemented)
        return neighbors

    def update_tabu_list(self, move: Move):
        # Add the new move to the tabu list and update tenures
        self.tabu_list.add(move)
        self.tabu_tenures[move] = self.tenure
        # Decrease tenures and remove expired moves
        expired_moves = [m for m, tenure in self.tabu_tenures.items() if tenure <= 1]
        for m in expired_moves:
            self.tabu_list.remove(m)
            del self.tabu_tenures[m]
        for m in self.tabu_list:
            self.tabu_tenures[m] -= 1

    def aspiration_criteria_met(self, solution: Solution) -> bool:
        # Check if solution meets the aspiration criteria
        return self.evaluate_solution(solution) < self.evaluate_solution(self.best_solution)
