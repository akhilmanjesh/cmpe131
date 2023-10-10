def cacti_number(func):
    def wrapper(plot):
        def is_valid(i, j, rows, cols):
            return 0 <= i < rows and 0 <= j < cols

        count = 0
        
        rows = len(plot)
        cols = len(plot[0])
        
        for i in range(rows):
            for j in range(cols):
                if plot[i][j] == 0:
                    if (not is_valid(i-1, j, rows, cols) or plot[i-1][j] == 0) and \
                       (not is_valid(i+1, j, rows, cols) or plot[i+1][j] == 0) and \
                       (not is_valid(i, j-1, rows, cols) or plot[i][j-1] == 0) and \
                       (not is_valid(i, j+1, rows, cols) or plot[i][j+1] == 0):
                        count += 1

        return count

    return wrapper

