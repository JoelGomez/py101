"""
>>> test(922)
True
>>> test(914)
False
>>> test(854)
True
>>> test(72)
False
>>> test(68)
False
"""

def test(val: int):
    """_summary_
        Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
    Args:
        val (int): number to evaluate

    Returns:
        _type_: boolean
    """
    return val > (4**4) and val % 34 == 4

print(test(914))