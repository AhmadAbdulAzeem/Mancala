from board_state import Board
from algorithm import Algorithm
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

    def getAlphaBetaDepth(self, difficulity):
        if(difficulity == 1):
            depth = 1
        elif (difficulity == 2):
            depth = 4
        elif (difficulity == 3):
            depth = 9
        return depth

    def play(self, playerStrategy, player, board, difficulity, mode):
        pit_to_move= int()
        freeMove = True
        # Display the board
        board.print_board()
        flag = False
        depth = self.getAlphaBetaDepth(difficulity)

        while(freeMove):
            actions = board.getFilledPitsIndex(player)
            if(playerStrategy == self.HUMAN):
                while(1):
                    pit_to_move = int(input("Select PIT Number to Move:   "))
                    pit_to_move = pit_to_move - 1
                    if(pit_to_move in actions):
                        break
                    else:
                        print("You Entered Empty PIT Number to Move !")
            elif(playerStrategy == self.ALPHABETA):
                print("Alphabeta Running.........")
                search = Algorithm()
                pit_to_move = search.alphabetaAlgorithm(board, player, depth, mode)

            freeMove = board.Move(pit_to_move, player,mode)

            # Display the updated board
            if(not flag):
                flag = True
            else:
                #board.print_board()
                flag = False

            # Check if game is terminated
            if(board.isGameOver()):
                return True

            if(freeMove):
                print("player   ", player + 1, " gets another move")
                board.print_board()

    def start(self, playerStrategy1, playerStrategy2,player,Difficulity,mode):
        board = Board()
        gameOver = False


        while(1):
            currentPlayer = player
            gameOver = self.play(playerStrategy1, currentPlayer, board, Difficulity, mode)

            if(gameOver):
                break

            currentPlayer = not(player)
            gameOver = self.play(playerStrategy2, currentPlayer, board, Difficulity, mode)

            if(gameOver):
                break

        outcome, winner = board.getScore(currentPlayer)
        board.print_board()
        
        if(winner == 0):
            print("HUMAN wins..........")
        elif(winner == 1):
            print("COMPUTER wins..........")
        else:
            print("Draw........")


