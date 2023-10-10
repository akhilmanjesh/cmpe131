from cacti import cacti_number

@cacti_number
def main(plot):
    return plot

plot = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1]
]
print(main(plot))  
