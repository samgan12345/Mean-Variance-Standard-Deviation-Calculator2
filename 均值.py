import pandas as pd
import numpy as np

def calculate_matrix_statistics(numbers):
    if len(numbers) != 9:
        raise ValueError("The input numbers must be 9")

    matrix = np.array(numbers).reshape((3,3))

    matrix_mean = np.mean(matrix)
    matrix_variance = np.var(matrix)
    matrix_std_dev = np.std(matrix)
    matrix_max = np.max(matrix)
    matrix_min = np.min(matrix)
    matrix_sum = np.sum(matrix)

    row_means = np.mean(matrix,axis=1)
    col_means = np.mean(matrix,axis=0)

    row_variances = np.var(matrix, axis=1)
    col_variances = np.var(matrix, axis=0)

    row_std_devs = np.std(matrix, axis=1)
    col_std_devs = np.std(matrix, axis=0)
    
    row_maxs = np.max(matrix, axis=1)
    col_maxs = np.max(matrix, axis=0)
    
    row_mins = np.min(matrix, axis=1)
    col_mins = np.min(matrix, axis=0)
    
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)



    statistics = {
        'mean': [row_means.tolist(), col_means.tolist(), matrix_mean],
        'variance': [row_variances.tolist(), col_variances.tolist(), matrix_variance],
        'standard deviation': [row_std_devs.tolist(), col_std_devs.tolist(), matrix_std_dev],
        'max': [row_maxs.tolist(), col_maxs.tolist(), matrix_max],
        'min': [row_mins.tolist(), col_mins.tolist(), matrix_min],
        'sum': [row_sums.tolist(), col_sums.tolist(), matrix_sum]
    }
    

    return statistics

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
statistics = calculate_matrix_statistics(numbers)
print(statistics)





