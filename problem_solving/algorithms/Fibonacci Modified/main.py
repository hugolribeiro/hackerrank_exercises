# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    term = 3
    while term <= n:
        actual_number = t1 + t2**2
        t1 = t2
        t2 = actual_number
        term += 1
    return actual_number
