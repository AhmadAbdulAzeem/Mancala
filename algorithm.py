import copy
from board_state import Board


class Algorithm:
    def __init__(self):
        self.minMaxNodes = 0
        self.alphaBetaNodes = 0

    # AlphaBeta algorithm
    def calcMaxValue(self, state, player, depth, alpha, beta,mode):
        if (state.isGameOver()):
            x, y = state.getScore(player)
            return x
        if (depth==0):
            return state.evaluation(player)
        actions = state.getFilledPitsIndex(player)
        v = -200#alpha
        v1 = int()
        for action in actions:
            next_state = copy.deepcopy(state)
            is_turn = next_state.Result(action, player,mode)
            if (is_turn):
                v1 = self.calcMaxValue(next_state, player, depth, alpha, beta,mode)
            else:
                v1 = self.calcMinValue(next_state, player, depth - 1, alpha, beta,mode)
            v = max(v, v1)
            if (v >= beta):
                return v
            alpha = max(alpha, v)
        return v

    def calcMinValue(self, state, player, depth, alpha, beta,mode):
        if (state.isGameOver()):
            x, y = state.getScore(player)
            return x
        if (depth==0):
            return state.evaluation(player)
        opponent = 1 - player
        actions = state.getFilledPitsIndex(opponent)
        v = 200
        v1 = int()
        for action in actions:
            next_state = copy.deepcopy(state)
            is_turn = next_state.Result(action, opponent,mode)
            if (is_turn):
                v1 = self.calcMinValue(next_state, player, depth, alpha, beta,mode)
            else:
                v1 = self.calcMaxValue(next_state, player, depth - 1, alpha, beta,mode)
            v = min(v, v1)
            if (v <= alpha):
                return v
            beta = min(beta, v)
        return v

    def alphabetaAlgorithm(self, state, player, depth,mode):
        actions = state.getFilledPitsIndex(player)
        alphabetaNodes = 1
        alpha = -200
        beta = 200
        v = -200
        v1 = int()
        m = -1
        for action in actions:
            next_state = copy.deepcopy(state)
            is_turn = next_state.Result(action, player,mode)
            if (is_turn):
                v1 = self.calcMaxValue(next_state, player, depth, alpha, beta,mode)
            else:
                v1 = self.calcMinValue(next_state, player, depth - 1, alpha, beta,mode)
            if (v1 > v):
                v = v1
                m = action
            alpha = max(alpha, v)
        return m