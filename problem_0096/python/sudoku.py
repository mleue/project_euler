from copy import deepcopy


def cross(list1, list2):
    """Cross product of elements in list1 and elements in list2."""
    return [x+y for x in list1 for y in list2]


assignments = []
ROWS = "ABCDEFGHI"
COLS = "123456789"
BOXES = cross(ROWS, COLS)

#[['A1', 'A2', ...], ['B1', 'B2', ...], ..., ['I1', 'I2', ...]]
ROW_UNITS = [cross(row, COLS) for row in ROWS]

#[['A1', 'B1', ...], ['A2', 'B2', ...], ..., ['A9', 'B9', ...]]
COL_UNITS = [cross(ROWS, col) for col in COLS]

#[['A1', ..., 'C3'], ['D4', ..., 'F6'], ..., ['G7', ..., 'I9']]
SQU_UNITS = [cross(rows, cols) for rows in ('ABC', 'DEF', 'GHI') for cols in ('123', '456', '789')]

# DIAG_UNITS = [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'],
#               ['I1', 'H2', 'G3', 'F4', 'E5', 'D6', 'C7', 'B8', 'A9']]

UNITLIST = ROW_UNITS + COL_UNITS + SQU_UNITS # + DIAG_UNITS
UNITS = dict((box, [unit for unit in UNITLIST if box in unit]) for box in BOXES)
PEERS = dict((box, set(sum(UNITS[box], []))-set([box])) for box in BOXES)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def grid_values(sudokustring):
    """
    Convert a sudokustring into a dict of {square: char} with '123456789' for empties.
    Args:
        sudokustring - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'.
            If the box has no value, then the value will be '123456789'.
    """
    charslist = []
    digits = '123456789'
    for char in sudokustring:
        if char in digits:
            charslist.append(char)
        if char == '.':
            charslist.append(digits)
    return dict(zip(BOXES, charslist))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in BOXES)
    line = '+'.join(['-'*(width*3)]*3)
    for row in ROWS:
        print(''.join(values[row+c].center(width)+('|' if c in '36' else '') for c in COLS))
        if row in 'CF':
            print(line)
    return


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    for unit in UNITLIST:
        occurences = {}
        for box in unit:
            if len(values[box]) == 2:
                occurences[values[box]] = occurences.get(values[box], []) + [box]
        # Eliminate the naked twins as possibilities for their unit peers
        for twinvalue, boxes in occurences.items():
            if len(boxes) == 2:
                for box in unit:
                    if box not in boxes:
                        for val in twinvalue:
                            values[box] = values[box].replace(val, "")
    return values


def eliminate(values):
    """
    go through all boxes and if the box is solved, then
    eliminate that value from all boxes that are peers to that box
    """
    for box, value in values.items():
        if len(value) == 1:
            for peer in PEERS[box]:
                assign_value(values, peer, values[peer].replace(value, ""))


def only_choice(values):
    """
    go through all units and for every box that is not solved
    check if there is a unique value that only fits into one
    particular box, if yes apply it
    """
    digits = "123456789"
    for unit in UNITLIST:
        for digit in digits:
            countlist = []
            for box in unit:
                if digit in values[box]:
                    countlist.append(box)
            if len(countlist) == 1:
                assign_value(values, countlist[0], digit)


def reduce_puzzle(values):
    """
    run all constraint propagation functions to iteratively
    solve the sudoku
    """
    eliminate(values)
    only_choice(values)
    naked_twins(values)


def search(values):
    """
    run constraint propagation and use dfs once the solver stalls
    """
    while True:
        previous_values = deepcopy(values)
        reduce_puzzle(values)
        if is_solved(values):
            #print("SOLVED")
            # display(values)
            return values
        if is_equal(values, previous_values):
            #print("STALLED")
            # display(values)
            #get one unsolved box to use for dfs with a minimum number of choices left
            # TODO somehow depth-first-search here causes randomness for guessed
            # solutions
            _, dfsbox = min((len(values[box]), box) for box in BOXES if len(values[box]) > 1)
            for value in values[dfsbox]:
                try:
                    new_values = deepcopy(values)
                    assign_value(new_values, dfsbox, value)
                    solution = search(new_values)
                    if solution:
                      return solution
                except:
                    pass
            return False


def solve(sudokustring):
    """
    Find the solution to a Sudoku grid.
    Args:
        sudokustring(string): a string representing a sudoku grid.
            Example:
                '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(sudokustring)
    return search(values)


def is_solved(values):
    """
    checks if the sudoku is solved
    """
    return len("".join(values.values())) == len(values)


def is_equal(values1, values2):
    """
    checks if two sudoku dictionaries are equal
    """
    for box in BOXES:
        if values1[box] != values2[box]:
            return False
    return True
