import math


def alphabeta_max(current_game, alpha=-math.inf, beta=math.inf):
    """
    MAX player using Alpha-Beta pruning
    :param current_game: current game state
    :param alpha: best value MAX can guarantee so far
    :param beta: best value MIN can guarantee so far
    :return: (value, best_move)
    """
    # Base case: game ended
    if current_game.is_terminal():
        return current_game.get_score(), None
    
    v = -math.inf
    best_move = None
    moves = current_game.get_moves()
    
    for move in moves:
        # Recursive call to MIN player
        val, _ = alphabeta_min(move, alpha, beta)
        
        # Update best value and move
        if val > v:
            v = val
            best_move = move
        
        # Update alpha - MAX's best guaranteed value
        alpha = max(alpha, v)
        
        # Beta cutoff: prune remaining branches
        # MIN will never choose this path since v >= beta
        if v >= beta:
            return v, best_move
    
    return v, best_move


def alphabeta_min(current_game, alpha=-math.inf, beta=math.inf):
    """
    MIN player using Alpha-Beta pruning
    :param current_game: current game state
    :param alpha: best value MAX can guarantee so far
    :param beta: best value MIN can guarantee so far
    :return: (value, best_move)
    """
    # Base case: game ended
    if current_game.is_terminal():
        return current_game.get_score(), None
    
    v = math.inf
    best_move = None
    moves = current_game.get_moves()
    
    for move in moves:
        # Recursive call to MAX player
        val, _ = alphabeta_max(move, alpha, beta)
        
        # Update best value and move
        if val < v:
            v = val
            best_move = move
        
        # Update beta - MIN's best guaranteed value
        beta = min(beta, v)
        
        # Alpha cutoff: prune remaining branches
        # MAX will never choose this path since v <= alpha
        if v <= alpha:
            return v, best_move
    
    return v, best_move


def maximin(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move)
        if v < mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
    return v, best_move


def minimax(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move)
        if v > mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
    return v, best_move
