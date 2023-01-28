"""
>>> eval_list([19, 19, 15, 5, 5, 5, 1, 2])
True
>>> eval_list([19, 15, 5, 7, 5, 5, 2])
False
>>> eval_list([11, 12, 14, 13, 14, 13, 15, 14])
True
>>> eval_list([19, 15, 11, 7, 5, 6, 2])
False
"""


def eval_list(arr: list):
    """_summary_
        Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

    Args:
        arr (list): list of integeres to evaluate

    Returns:
        _type_: boolean
    """
    return len(arr) == 8 and arr.count(arr[4])== 3
        
    


print(eval_list([19, 19, 15, 5, 5, 5, 1, 2]))