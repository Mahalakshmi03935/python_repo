import logging
#defining calculate_probability function
def calculate_probability(n, letters, k):
    total_indices = n
    indices_with_target_letter = letters.count('a')
    probability = 1 - ((1 - indices_with_target_letter / total_indices) ** k)
    return round(probability, 4)

