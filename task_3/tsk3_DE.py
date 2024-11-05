import math
import unittest

def time_to_cyclic(hour):
    """
    Convert hour in 24-hour format to cyclic sine and cosine representation.
    
    Parameters:
    hour (float): The time in hours (0 - 24 scale)
    
    Returns:
    tuple: A tuple (sin_value, cos_value) representing the cyclic time.
    """
    radians = (hour / 24) * 2 * math.pi
    sin_value = math.sin(radians)
    cos_value = math.cos(radians)
    return sin_value, cos_value

def calculate_cyclic_time_difference(hour1, hour2):
    """
    Calculate the cyclic time difference between two times in 24-hour format.
    
    Parameters:
    hour1 (float): First time in hours (0 - 24 scale)
    hour2 (float): Second time in hours (0 - 24 scale)
    
    Returns:
    float: The cyclic time difference in hours.
    """
    sin1, cos1 = time_to_cyclic(hour1)
    sin2, cos2 = time_to_cyclic(hour2)
    
    dot_product = sin1 * sin2 + cos1 * cos2
    angle_difference = math.acos(dot_product) 
    
    hours_difference = (angle_difference * 24) / (2 * math.pi)
    
    return hours_difference

class TestCyclicTimeDifference(unittest.TestCase):
    def test_midnight_and_noon(self):
        self.assertAlmostEqual(calculate_cyclic_time_difference(0, 12), 12, places=2)
        
    def test_one_hour_apart(self):
        self.assertAlmostEqual(calculate_cyclic_time_difference(1, 2), 1, places=2)
        
    def test_across_midnight(self):
        self.assertAlmostEqual(calculate_cyclic_time_difference(23, 1), 2, places=2)
        
    def test_same_time(self):
        self.assertAlmostEqual(calculate_cyclic_time_difference(5, 5), 0, places=2)
        
    def test_opposite_hours(self):
        self.assertAlmostEqual(calculate_cyclic_time_difference(3, 15), 12, places=2)

if __name__ == '__main__':
    unittest.main()
