from state import State
from search import Search

CUTOFF_DEPTH_ALPHABETA = 8
WIN, LOSS, DRAW = 1, 2, 3
RANDOM, HUMAN, MINMAX, ALPHABETA = 0, 1, 2, 3

PLAYER1, PLAYER2 = 0, 1


startegyTyps = {"random": RANDOM, "human": HUMAN,
                "minmax": MINMAX, "alphabeta": ALPHABETA}


def evaluate(playerStrategy, player, state):
    move = int()
    isFreeTurn = True
    # Display the board
    state.print_board()

    while(isFreeTurn):
        actions = state.action(player)
        if(playerStrategy == HUMAN):
            while(1):
                move = int(input("Enter move:   "))
                move = move - 1
                if(move in actions):
                    break
                else:
                    print("Illegal mov")
        elif(playerStrategy == ALPHABETA):
            print("Alphabeta.........")
            search = Search()
            move = search.alphabetaDecision(
                state, player, CUTOFF_DEPTH_ALPHABETA)

        isFreeTurn = state.Result(move, player)
        # Display the updated board
        state.print_board()

        # Check if game is terminated
        if(state.terminalTest()):
            return True

        if(isFreeTurn):
            print("player   ", player+1, " gets another move")


def run_game(playerStrategy1, playerStrategy2):
    currentState = State()
    isTerminated = False
    currentPlayer = int()

    while(1):
        currentPlayer = PLAYER1
        isTerminated = evaluate(playerStrategy1, currentPlayer, currentState)

        if(isTerminated):
            break

        currentPlayer = PLAYER2
        isTerminated = evaluate(playerStrategy2, currentPlayer, currentState)

        if(isTerminated):
            break

    outcome, winner = currentState.utility(currentPlayer)
    if(winner == 0):
        print("Player1 wins..........")
    elif(winner == 1):
        print("Player2 wins..........")
    else:
        print("Draw........")

run_game(HUMAN, ALPHABETA)