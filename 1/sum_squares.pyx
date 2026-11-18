def sum_squares_c(list lst):
    cdef int i, n = len(lst)
    cdef double s = 0.0, x
    for i in range(n):
        x = lst[i]
        s += x * x
    return s