"""
Question: Square(n) Sum

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

"""

def square_sum(numbers):
    bs_list = []
    for bs in numbers:
        bs_list.append(bs ** 2)
    return sum(bs_list)