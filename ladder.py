def my_steps(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    ways = [0, 1, 2] + [0] * (n-2)
    
    for i in range(3, n+1):
        ways[i] = ways[i-1] + ways[i-2]
    
    return ways[n]

