from board_state import State
from search import Search
WIN, LOSS, DRAW = 1, 2, 3
HUMAN, ALPHABETA = 0, 1
PLAYER1, PLAYER2 = 0, 1
startegyTyps = { "human": HUMAN,
                 "alphabeta": ALPHABETA}


class Game:
    def __init__(self):

        self.HUMAN = 0
        self.ALPHABETA = 1
        self.PLAYER1 = 0
        self.PLAYER2 = 1

    def play(self, playerStrategy, player, state,Difficulity):
        move = int()
        freeMove = True
        # Display the board
        state.print_board()
        flag = False
        if(Difficulity==1):
            CUTOFF_DEPTH_ALPHABETA=1
        if (Difficulity == 2):
            CUTOFF_DEPTH_ALPHABETA = 4
        if (Difficulity == 3):
            CUTOFF_DEPTH_ALPHABETA = 8
        while(freeMove):
            actions = state.action(player)
            if(playerStrategy == self.HUMAN):
                while(1):
                    move = int(input("Enter your move:   "))
                    move = move - 1
                    if(move in actions):
                        break
                    else:
                        print("You entered wrong move")
            elif(playerStrategy == self.ALPHABETA):
                print("Alphabeta Running.........")
                search = Search()
                move = search.alphabetaDecision(
                    state, player, CUTOFF_DEPTH_ALPHABETA)

            freeMove = state.Result(move, player)

            # Display the updated board
            if(not flag):
                flag = True
            else:
                state.print_board()
                flag = False

            # Check if game is terminated
            if(state.terminalTest()):
                return True

            if(freeMove):
                print("player   ", player + 1, " gets another move")
                state.print_board()

    def start(self, playerStrategy1, playerStrategy2,player,Difficulity):
        board = State()
        gameOver = False
        currentPlayer = int()

        while(1):
            currentPlayer = player
            gameOver = self.play(
                playerStrategy1, currentPlayer, board,Difficulity)

            if(gameOver):
                break

            currentPlayer = not(player)
            gameOver = self.play(
                playerStrategy2, currentPlayer, board,Difficulity)

            if(gameOver):
                break

        outcome, winner = board.utility(currentPlayer)
        if(winner == 0):
            print("HUMAN wins..........")
        elif(winner == 1):
            print("COMPUTER wins..........")
        else:
            print("Draw........")


