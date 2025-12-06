def count_moves_for_both_players(state):
    current_player = state.get_curr_player()
    
    current_moves = len(state.potential_moves())
    
    state.set_curr_player((current_player % 2) + 1)
    opponent_moves = len(state.potential_moves())
    
    state.set_curr_player(current_player)
    
    return (current_moves, opponent_moves)

def base_heuristic(curr_state):
    (current_moves, opponent_moves) = count_moves_for_both_players(curr_state)
    return current_moves - opponent_moves
   


def advanced_heuristic(curr_state):
    return 0
