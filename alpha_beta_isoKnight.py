import math


def alphabeta_max(current_game):
    """
    Wrapper: run alpha-beta starting from a MAX node.
    Uses the alpha-beta implementation inside maximin().
    """
    return maximin(current_game)


def alphabeta_min(current_game):
    """
    Wrapper: run alpha-beta starting from a MIN node.
    Uses the alpha-beta implementation inside minimax().
    """
    return minimax(current_game)


def maximin(current_game):
    """
    MAX layer with alpha-beta pruning.
    Signature stays: maximin(current_game)
    """

    def _max(node, alpha, beta):
        # Terminal node: return its score
        if node.is_terminal():
            return node.get_score(), None

        v = -math.inf
        best_move = None

        for move in node.get_moves():
            # recurse to MIN layer
            mx, _ = _min(move, alpha, beta)

            if v < mx:
                v = mx
                best_move = move

            # add code here for alpha-beta algorithm
            # beta cutoff: MIN can already force a value <= beta
            if v >= beta:
                return v, None

            # update alpha (best value MAX can guarantee so far)
            alpha = max(alpha, v)

        return v, best_move

    def _min(node, alpha, beta):
        # Terminal node
        if node.is_terminal():
            return node.get_score(), None

        v = math.inf
        best_move = None

        for move in node.get_moves():
            mx, _ = _max(move, alpha, beta)

            if v > mx:
                v = mx
                best_move = move

            # alpha cutoff: MAX can already force a value >= alpha
            if v <= alpha:
                return v, None

            # update beta (best value MIN can guarantee so far)
            beta = min(beta, v)

        return v, best_move

    # initial call: MAX at root with full alpha/beta range
    return _max(current_game, -math.inf, math.inf)


def minimax(current_game):
    """
    MIN layer with alpha-beta pruning.
    Signature stays: minimax(current_game)
    """

    def _max(node, alpha, beta):
        if node.is_terminal():
            return node.get_score(), None

        v = -math.inf
        best_move = None

        for move in node.get_moves():
            mx, _ = _min(move, alpha, beta)

            if v < mx:
                v = mx
                best_move = move

            # add code here for alpha-beta algorithm (MAX side)
            if v >= beta:
                return v, None

            alpha = max(alpha, v)

        return v, best_move

    def _min(node, alpha, beta):
        if node.is_terminal():
            return node.get_score(), None

        v = math.inf
        best_move = None

        for move in node.get_moves():
            mx, _ = _max(move, alpha, beta)

            if v > mx:
                v = mx
                best_move = move

            # add code here for alpha-beta algorithm (MIN side)
            if v <= alpha:
                return v, None

            beta = min(beta, v)

        return v, best_move

    # root is MIN
    return _min(current_game, -math.inf, math.inf)
