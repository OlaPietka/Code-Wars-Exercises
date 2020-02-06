def row_sum_odd_numbers(n):
    s = n*(n+1)/2
    return sum([2 * i - 1 for i in range(s, s-n, -1)])