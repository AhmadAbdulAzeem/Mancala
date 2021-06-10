import copy
from board_state import State


class Search:
    def __init__(self):
        self.minMaxNodes = 0
        self.alphaBetaNodes = 0

    # AlphaBeta algorithm
    def maxValue(self, state, player, depth, alpha, beta):
        if (state.terminalTest()):
            x, y = state.utility(player)
            return x
        if (depth==0):
            return state.evaluation(player)
        actions = state.action(player)
        v = -200
        v1 = int()
        for action in actions:
            next_state = copy.deepcopy(state)
            is_turn = next_state.Result(action, player)
            if (is_turn):
                v1 = self.maxValue(next_state, player, depth, alpha, beta)
            else:
                v1 = self.minValue(next_state, player, depth - 1, alpha, beta)
            v = max(v, v1)
            if (v >= beta):
                return v
            alpha = max(alpha, v)
        return v

    def minValue(self, state, player, depth, alpha, beta):
        if (state.terminalTest()):
            x, y = state.utility(player)
            return x
        if (depth==0):
            return state.evaluation(player)
        opponent = 1 - player
        actions = state.action(opponent)
        v = 200
        v1 = int()
        for action in actions:
            next_state = copy.deepcopy(state)
            is_turn = next_state.Result(action, opponent)
            if (is_turn):
                v1 = self.minValue(next_state, player, depth, alpha, beta)
            else:
                v1 = self.maxValue(next_state, player, depth - 1, alpha, beta)
            v = min(v, v1)
            if (v <= alpha):
                return v
            beta = min(beta, v)
        return v

    def alphabetaDecision(self, state, player, depth):
        actions = state.action(player)
        alphabetaNodes = 1
        alpha = -200
        beta = 200
        v = -200
        v1 = int()
        m = -1
        for action in actions:
            next_state = copy.deepcopy(state)
            is_turn = next_state.Result(action, player)
            if (is_turn):
                v1 = self.maxValue(next_state, player, depth, alpha, beta)
            else:
                v1 = self.minValue(next_state, player, depth - 1, alpha, beta)
            if (v1 > v):
                v = v1
                m = action
            alpha = max(alpha, v)
        return m