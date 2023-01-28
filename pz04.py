"""
>>> test(2)
[2, 4]

>>> test(10)
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

>>> test(3)
[3, 5, 7]

>>> test(17)
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
"""

def test(n: int):
    """_summary_
    We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile   
    Args:
        n (int): number of stones
    Returns: a list of piles of stones
    """
    arr = []

    for i in range(n):
        arr.append(n)
        n += 2
    return arr

print(test(10))