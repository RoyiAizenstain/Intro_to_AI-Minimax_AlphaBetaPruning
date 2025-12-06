import numpy as np

# List of all possible knight moves (global constant for performance)
KNIGHT_OFFSETS = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

def get_degree(grid, r, c, rows, cols):
    """
    Fast helper function:
    Calculates how many empty squares can be reached from position (r,c).
    
    :param grid: game board
    :param r: row position
    :param c: column position
    :param rows: total rows in grid
    :param cols: total columns in grid
    :return: number of reachable empty squares
    """
    count = 0
    for dr, dc in KNIGHT_OFFSETS:
        nr, nc = r + dr, c + dc
        # Check bounds and if square is empty (0)
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
            count += 1
    return count

def evaluate_player(grid, pos, rows, cols):
    """
    Calculates score for a single player based on position and near future.
    
    Considers:
    1. Immediate mobility (current legal moves)
    2. Future potential (sum of degrees from next positions)
    3. Center bonus (prefer staying near center)
    
    :param grid: game board
    :param pos: player position (row, col)
    :param rows: total rows
    :param cols: total columns
    :return: player's score
    """
    r, c = pos
    
    # 1. Immediate mobility: where can I move now?
    # Store the list of valid moves to check their "next generation"
    valid_moves = []
    for dr, dc in KNIGHT_OFFSETS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
            valid_moves.append((nr, nc))
            
    current_mobility = len(valid_moves)
    
    # If no moves available - we lost (very bad score)
    if current_mobility == 0:
        return -1000

    # 2. Future potential (Sum of degrees):
    # For each possible move, how many moves will I have from there?
    future_mobility = 0
    for move_r, move_c in valid_moves:
        future_mobility += get_degree(grid, move_r, move_c, rows, cols)
        
    # 3. Center bonus:
    # Prefer staying close to the center of the board
    center_r, center_c = rows / 2, cols / 2
    dist_from_center = abs(r - center_r) + abs(c - center_c)
    center_penalty = dist_from_center * 0.1  # Low weight
    
    # Weighted formula:
    # present * 10 + future * 1 - distance from center
    score = (current_mobility * 10) + future_mobility - center_penalty
    return score


def advanced_heuristic(state):
    """
    Advanced and fast heuristic:
    Calculates the difference between my score and opponent's score.
    
    Higher score = better position for current player
    
    :param state: game_state object
    :return: score difference (my_score - opponent_score)
    """
    # Extract raw data (faster than using wrapper functions)
    grid = state.get_grid()
    rows, cols = grid.shape
    locs = state.get_player_locations()
    
    # Who is the current player and who is the opponent?
    curr_player_idx = state.get_curr_player()
    opponent_idx = 2 if curr_player_idx == 1 else 1
    
    p_curr_pos = locs[curr_player_idx]
    p_opp_pos = locs[opponent_idx]
    
    # Calculate scores
    my_score = evaluate_player(grid, p_curr_pos, rows, cols)
    opp_score = evaluate_player(grid, p_opp_pos, rows, cols)
    
    return my_score - opp_score

def count_moves_for_player(state, player_idx):
    """
    Helper function: counts moves for a specific player 
    (without permanently changing the turn in state).
    
    :param state: game_state object
    :param player_idx: player number (1 or 2)
    :return: number of legal moves for that player
    """
    # Save the original current player
    original_turn = state.get_curr_player()
    
    # Temporarily set turn to the requested player to check moves
    state.set_curr_player(player_idx)
    moves_count = len(state.get_moves())  # Ensure this is the correct function
    
    # Restore the original turn
    state.set_curr_player(original_turn)
    
    return moves_count

def base_heuristic(state):
    """
    Basic heuristic: always returns (player 1 moves) minus (player 2 moves).
    
    Simple mobility-based evaluation:
    - Positive value = good for player 1
    - Negative value = good for player 2
    
    :param state: game_state object
    :return: difference in number of legal moves
    """
    p1_moves = count_moves_for_player(state, 1)
    p2_moves = count_moves_for_player(state, 2)
    
    return p1_moves - p2_moves