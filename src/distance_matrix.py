import numpy as np


class DistanceMatrixSingleton:
    _instance = None
    _distance_matrix = None

    def __new__(cls, customers=None):
        if cls._instance is None:
            cls._instance = super(DistanceMatrixSingleton, cls).__new__(cls)
            if customers is not None:
                cls._distance_matrix = cls._calculate_distance_matrix(customers)
        return cls._instance

    @staticmethod
    def _calculate_distance_matrix(customers):
        n = len(customers)
        distance_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i != j:
                    dist = np.sqrt((customers[i].x_coord - customers[j].x_coord)**2 +
                                   (customers[i].y_coord - customers[j].y_coord)**2)
                    distance_matrix[i][j] = dist
        return distance_matrix

    @classmethod
    def get_distance_matrix(cls):
        """
        Return the existing distance matrix.

        :return: A 2D NumPy array representing the distance matrix.
        """
        if cls._distance_matrix is None:
            raise ValueError("Distance matrix has not been initialized.")
        return cls._distance_matrix
