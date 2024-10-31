import numpy as np

def generate_random_data(mean, variance, num_samples):
    """
    Generates random threat scores between mean-variance and mean+variance+1 (inclusive)
    """
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_aggregated_threat_score(department_data):
    """
    Calculates the aggregated threat score for a company.

    Args:
        department_data: A list of tuples, where each tuple contains:
            - Department name
            - Importance factor (1-5)
            - List of user threat scores (0-90)

    Returns:
        The aggregated threat score.
    """

    total_users = 0
    weighted_sum = 0
    std_dev_sum = 0

    for department, importance, scores in department_data:
        total_users += len(scores)
        weighted_sum += np.mean(scores) * importance
        std_dev_sum += np.std(scores) * importance

    weighted_avg = weighted_sum / total_users
    std_dev_avg = std_dev_sum / total_users

    # Consider adding a penalty factor for high standard deviation:
    penalty_factor = 1 + (std_dev_avg / 10)  # Adjust the divisor as needed
    final_score = weighted_avg * penalty_factor

    return min(max(final_score, 0), 90)  # Ensure score is within 0-90 range

# Example usage
department_data = [
    ("Engineering", 5, generate_random_data(50, 15, 100)),
    ("Marketing", 3, generate_random_data(30, 10, 50)),
    ("Finance", 4, generate_random_data(40, 12, 80)),
    ("HR", 2, generate_random_data(20, 8, 30)),
    ("Science", 5, generate_random_data(60, 20, 120))
]

aggregated_score = calculate_aggregated_threat_score(department_data)
print("Aggregated Threat Score:", aggregated_score)