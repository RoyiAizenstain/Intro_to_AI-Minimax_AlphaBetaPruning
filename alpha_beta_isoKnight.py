import math


import math

def alphabeta_max(current_game):
    """
    Alpha-beta pruning starting from a MAX node.
    Returns a tuple (value, best_move) where:
      - value is the minimax score of the given game state
      - best_move is the move (child state) that leads to that optimal score
    """

    def _max(node, alpha, beta):
        """
        Recursive helper for MAX nodes in alpha-beta search.
        node  : current game state
        alpha : best score already guaranteed to the MAX player
        beta  : best score already guaranteed to the MIN player
        """
        # If we reached a terminal node, return its score and no move
        if node.is_terminal():
            return node.get_score(), None

        v = -math.inf     # current best value for MAX
        best_move = None  # track which move produced v

        # Explore all possible moves (children states)
        for move in node.get_moves():
            # Recurse into MIN player
            child_val, _ = _min(move, alpha, beta)

            # Update best value and move for MAX
            if child_val > v:
                v = child_val
                best_move = move

            # Beta cutoff: MIN already has something <= beta,
            # and since v >= beta, MIN will never choose this branch
            if v >= beta:
                return v, best_move

            # Update alpha
            alpha = max(alpha, v)

        return v, best_move

    def _min(node, alpha, beta):
        """
        Recursive helper for MIN nodes in alpha-beta search.
        node  : current game state
        alpha : best score already guaranteed to the MAX player
        beta  : best score already guaranteed to the MIN player
        """
        if node.is_terminal():
            return node.get_score(), None

        v = math.inf      # current best value for MIN
        best_move = None  # track which move produced v

        for move in node.get_moves():
            # Recurse into MAX player
            child_val, _ = _max(move, alpha, beta)

            # Update best value and move for MIN
            if child_val < v:
                v = child_val
                best_move = move

            # Alpha cutoff: MAX already has something >= alpha,
            # and since v <= alpha, MAX will never choose this branch
            if v <= alpha:
                return v, best_move

            # Update beta
            beta = min(beta, v)

        return v, best_move

    # Initial alpha, beta values start as negative/positive infinity
    return _max(current_game, -math.inf, math.inf)



def alphabeta_min(current_game):
    """
    Alpha-beta pruning starting from a MIN node.
    Returns a tuple (value, best_move) where:
      - value is the minimax score of the given game state
      - best_move is the move that results in that minimal value

    """

    def _max(node, alpha, beta):
        """
        Helper function for MAX nodes.
        """
        if node.is_terminal():
            return node.get_score(), None

        v = -math.inf
        best_move = None

        for move in node.get_moves():
            child_val, _ = _min(move, alpha, beta)

            if child_val > v:
                v = child_val
                best_move = move

            if v >= beta:
                return v, best_move

            alpha = max(alpha, v)

        return v, best_move

    def _min(node, alpha, beta):
        """
        Helper function for MIN nodes.
        """
        if node.is_terminal():
            return node.get_score(), None

        v = math.inf
        best_move = None

        for move in node.get_moves():
            child_val, _ = _max(move, alpha, beta)

            if child_val < v:
                v = child_val
                best_move = move

            if v <= alpha:
                return v, best_move

            beta = min(beta, v)

        return v, best_move

    return _min(current_game, -math.inf, math.inf)



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
