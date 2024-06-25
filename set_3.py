'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]['following']:
        # Check if the 'to_member' is also following the 'from_member'
        if from_member in social_graph[to_member]['following']:
            return "friends"
        else:
            return "follower"
    # Check if the 'to_member' is following the 'from_member'
    elif from_member in social_graph[to_member]['following']:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    size = len(board)

    # Check rows for a winner
    for row in board:
        if all(symbol == row[0] and symbol != '' for symbol in row):
            return row[0]

    # Check columns for a winner
    for col in range(size):
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(size)):
            return board[0][col]

    # Check top-left to bottom-right diagonal
    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(size)):
        return board[0][0]

    # Check top-right to bottom-left diagonal
    if all(board[i][size - 1 - i] == board[0][size - 1] and board[i][size - 1 - i] != '' for i in range(size)):
        return board[0][size - 1]

    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while True:
        # Find the next stop and the travel time to it
        for (start, end), leg in route_map.items():
            if start == current_stop:
                total_time += leg['travel_time_mins']
                current_stop = end
                break
        
        # If we reach the second stop, return the total time accumulated
        if current_stop == second_stop:
            return total_time