from rich.table import Table
from rich.console import Console
class Board:
    def __init__(self):
        self.PITS = 6
        self.TOTAL_PITS = 12
        self.BOARD_SIZE = 14
        self.PLAYER1 = 0
        self.PLAYER2 = 1
        self.mancala_board = [4, 4, 4, 4, 4, 4, 0,
                              4, 4, 4, 4, 4, 4, 0]

# stones per pit

    def evaluation(self, player):
        count_heuristic1 = self.mancala_board[self.PITS + (self.PITS + 1) * player] - self.mancala_board[
            self.PITS + (self.PITS + 1) * (1 - player)]
        count_heuristic2 = 0
        limit1 = (self.PITS + 1) * player
        limit2 = (self.PITS + 1) * (1 - player)
        for i in range(self.PITS):
            count_heuristic2 = count_heuristic2 + abs((int((not (not self.mancala_board[i + limit1]))) - int((not (not self.mancala_board[i + limit2])))))
        return count_heuristic1 + count_heuristic2


    # return a list of indeces of non empty pits
    def getFilledPitsIndex(self, player):
        moves = []
        limit = 7 * player
        for i in range(6):
            if(self.mancala_board[i+limit]):
                moves.append(i)
        return moves

    def Result(self, move, player,mode):
        precomputed_limit = (self.PITS + 1) * player #0
        i = move + precomputed_limit
        stones = self.mancala_board[i]
        self.mancala_board[i] = 0

        opponent_store = self.TOTAL_PITS + 1 - precomputed_limit #compute index of opponent store
        while (stones):
            i = (i + 1) % self.BOARD_SIZE

            if (i == opponent_store): #rule game
                continue
            self.mancala_board[i] = self.mancala_board[i] + 1
            stones = stones - 1

        # Check if last stone landed in player's store
        # In this case the player gets another turn
        if (i == self.PITS + precomputed_limit):
            return True
        if(mode):
            # Stealing
            # Check if last stone landed in player's empty bin and opposite player's bin has at least one stone
            # In this case all the stones in the opponent's bins go to the player's store
            if (i < (self.PITS + precomputed_limit) and i >= precomputed_limit and self.mancala_board[i] == 1 and
                    self.mancala_board[self.TOTAL_PITS - i] > 0):
                # Collect stones from player's pit and opponent's pit and put them in player's store
                self.mancala_board[self.PITS + precomputed_limit] = self.mancala_board[self.PITS +
                                                                                       precomputed_limit] + (
                                                                                self.mancala_board[self.TOTAL_PITS - i] + 1)
                # empty player's pit and opponent's pit
                self.mancala_board[self.TOTAL_PITS - i] = self.mancala_board[i] = 0
            return False


    def getScore(self, expectedPlayer):
        precomputed_limit = (self.PITS + 1) * expectedPlayer
        for i in range(self.PITS):
            self.mancala_board[precomputed_limit + 6] = self.mancala_board[precomputed_limit +
                                                                           6] + self.mancala_board[
                                                            i + precomputed_limit]

        diff = self.mancala_board[6] - self.mancala_board[13]
        if (diff < 0):
            return abs(diff), 1
        elif (diff > 0):
            return abs(diff), 0

        else:
            return abs(diff), 2

    # The game is over when one player’s pits are completely empty.
    def isGameOver(self):
        if (any(self.mancala_board[0:6]) != 0 and any(self.mancala_board[7:13]) != 0):
            return False
        return True

    def print_board(self):
        table = Table()

        table.add_column("Store")
        table.add_column("Pit")
        table.add_column("Pit")
        table.add_column("Pit")
        table.add_column("Pit")
        table.add_column("Pit")
        table.add_column("Pit")
        table.add_column("Store")
        table.add_column("Player")

        table.add_row(str(self.mancala_board[13]), str(self.mancala_board[7]), str(self.mancala_board[8]),
                      str(self.mancala_board[9]),
                      str(self.mancala_board[10]), str(self.mancala_board[11]), str(self.mancala_board[12]), "--", "Computer")
        table.add_row("--", str(self.mancala_board[0]), str(self.mancala_board[1]), str(self.mancala_board[2]), str(self.mancala_board[3]),
                      str(self.mancala_board[4]), str(self.mancala_board[5]), str(self.mancala_board[6]), "Human")

        console = Console()
        console.print(table)


















    #print('############################################')
        #new = self.mancala_board[7:]
        #print('COMPTUER -->', new[::-1])
        #print('HUMAN    -->', self.mancala_board[0:7])
        #print('############################################')


