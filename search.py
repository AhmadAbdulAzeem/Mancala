import copy
from state import State


class Search:
    def __init__(self):
        self.minMaxNodes = 0
        self.alphaBetaNodes = 0

    # AlphaBeta algorithm
    def maxValue(self, state, player, depth, alpha, beta):
        if (state.terminal_test()):
            x,0 = state.utility(player)
            return x
        if (state.cutoffTest(depth)):
            return state.eval(player)
        actions = state.action(player)
        v = -128
        v1 = int()
        for action in actions:
            next_state = copy.deepcopy(state)
            is_turn = next_state.result(action, player)
            if(is_turn):
                v1 = self.maxValue(next_state, player, depth, alpha, beta)
            else:
                v1 = self.minValue(next_state, player, depth - 1, alpha, beta)
            v = max(v,v1)
            if(v >= beta):
                return v
            alpha = max(alpha, v)
        return v
