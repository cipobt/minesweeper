# global variables
field = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]


# function
def minesweeper(grid):
    """
    Replacing all dashes with counters for all mines around the indexed position
    :param grid: which is the global variable field (the 2D list provided in the PDF)
    :return: new_grid which is a 2D list with the dashes replaced by counters
    """

    size = len(grid)

    new_grid = [[" "] * size for _ in range(size)]

    # using nested for loops to move through both grids
    for row in range(size):
        for col in range(size):

            numb_mines = 0

            if grid[row][col] == "#":
                new_grid[row][col] = "#"
                continue

            else:

                # following the PDF for this task and a mentoring session with Chris Smith I've decided to use 8 if statements
                # to check the cells around the current position, each if statement relating to a cardinal point

                # North (up)
                if row - 1 >= 0:  # making sure the row index doesn't go out of bounds for all the upper (North) cells
                    if grid[row - 1][col] == "#":
                        numb_mines += 1

                    # Northwest
                    if 0 < col - 1:
                        if grid[row - 1][col - 1] == "#":
                            numb_mines += 1

                    # Northeast
                    if col + 1 < size:
                        if grid[row - 1][col + 1] == "#":
                            numb_mines += 1

                # West (left)
                if col - 1 > 0:
                    if grid[row][col - 1] == "#":
                        numb_mines += 1

                # East (right)
                if col + 1 < size:
                    if grid[row][col + 1] == "#":
                        numb_mines += 1

                # South (down)
                if row + 1 < size:  # making sure the row index doesn't go out of bounds for all the lower (South) cells
                    if grid[row + 1][col] == "#":
                        numb_mines += 1

                    # Southwest
                    if 0 < col - 1:
                        if grid[row + 1][col - 1] == "#":
                            numb_mines += 1

                    # Southeast
                    if col + 1 < size:
                        if grid[row + 1][col + 1] == "#":
                            numb_mines += 1

                new_grid[row][col] = str(numb_mines)

    return new_grid


# main
print("\nGiven this minefield: \n")

size = len(field)

for row in range(size):
    print(field[row])

result = minesweeper(field)

print("\nThe minesweeper creates the following grid: \n")

for row in range(size):
    print(result[row])
