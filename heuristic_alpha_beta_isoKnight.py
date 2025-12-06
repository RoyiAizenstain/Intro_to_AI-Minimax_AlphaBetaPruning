import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth=3, alpha=-math.inf, beta=math.inf):
    """
    Implements the MAX player turn with Alpha-Beta pruning and Heuristic evaluation.
    """
    global h
    h = _heuristic

    # Base case 1: The game has ended
    if current_game.is_terminal():
        return current_game.get_score(), None

    # Base case 2: Maximum depth reached - evaluate using heuristic
    if depth == 0:
        return h(current_game), None

    v = -math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        # Recursive call to the MIN player
        # Pass the current alpha and beta values down the tree
        val, _ = alphabeta_min_h(move, _heuristic, depth - 1, alpha, beta)

        # Maximize the value
        if val > v:
            v = val
            best_move = move

        # Update alpha: the best value MAX can guarantee so far
        alpha = max(alpha, v)

        # Pruning condition (Beta Cut-off):
        # If the current value (v) is greater than or equal to beta,
        # the MIN player (at the parent node) will strictly avoid this path.
        # Therefore, there is no need to search further.
        if v >= beta:
            return v, best_move

    return v, best_move


def alphabeta_min_h(current_game, _heuristic, depth=3, alpha=-math.inf, beta=math.inf):
    """
    Implements the MIN player turn with Alpha-Beta pruning and Heuristic evaluation.
    """
    global h
    h = _heuristic

    # Base case 1: The game has ended
    if current_game.is_terminal():
        return current_game.get_score(), None

    # Base case 2: Maximum depth reached - evaluate using heuristic
    if depth == 0:
        return h(current_game), None

    v = math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        # Recursive call to the MAX player
        val, _ = alphabeta_max_h(move, _heuristic, depth - 1, alpha, beta)

        # Minimize the value
        if val < v:
            v = val
            best_move = move

        # Update beta: the lowest value MIN can guarantee so far
        beta = min(beta, v)

        # Pruning condition (Alpha Cut-off):
        # If the current value (v) is less than or equal to alpha,
        # the MAX player (at the parent node) will strictly avoid this path.
        # Therefore, there is no need to search further.
        if v <= alpha:
            return v, best_move

    return v, best_move


def maximin(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1)
        if v < mx:
            v = mx
            best_move = move
    return v, best_move


def minimax(current_game, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1)
        if v > mx:
            v = mx
            best_move = move

    return v, best_move
