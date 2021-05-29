
PITS = 6
TOTAL_PITS = 12
BOARD_SIZE = 14  # 0->5 player1 pits, 6 player1 store, 7->12 player2 pits, 13 player2 store

PLAYER1, PLAYER2 = 0, 1

mancala_board = [0, 5, 5, 5, 5, 4, 0,\
                 4, 4, 4, 4, 4, 4, 0]  # stones per pit

# Difference between players store and oppponent store
def heurestic1(player):
    return mancala_board[PITS + (PITS + 1) * player] - mancala_board[PITS + (PITS + 1) * (1 - player)]

# Difference between the number of non-empty pits in player's row and opponent's row
def heursitic2(player):
    count = 0
    limit1 = (PITS + 1) * player
    limit2 = (PITS + 1) * (1 - player)
    for i in range(PITS):
        count = count + abs((int((not (not mancala_board[i + limit1]))) - int((not (not mancala_board[i + limit2])))))
    return count

# Number of stones on player's board with decreasing probability from 0 - 5
# This heuristic gives more weight to the stones on the far left of the player's store
def heuristic3(player):
    count = 0
    limit1 = (PITS + 1) * player
    for i in range(PITS):
        count = count + 0.1 * (PITS - i) * (mancala_board[i + limit1])
    return count

def evaluation(player):
    return heurestic1(player) + heuristic3(player)

def cutOffTest(depth):
    return (depth == 0)

def action(player, mancala_board):
    moves = []
    precomputed_limit = (PITS + 1) * player
    for i in range(PITS):
        if(mancala_board[i+precomputed_limit]):
            print(mancala_board[i+precomputed_limit])
            moves.append(i)
            print("index", i)

    return moves


def Result(move, player, mancala_board):
    precomputed_limit = (PITS + 1) * player
    i = move + precomputed_limit
    stones = mancala_board[i]
    mancala_board[i] = 0

    opponent_store = TOTAL_PITS + 1 - precomputed_limit
    while (stones):
        i = (i + 1) % BOARD_SIZE

        if (i == opponent_store):
            continue
        mancala_board[i] = mancala_board[i]+1
        stones = stones - 1

    # Check if last stone landed in player's store
    # In this case the player gets another turn
    if (i == PITS + precomputed_limit):
        return True

    # Stealing
    # Check if last stone landed in player's empty bin and opposite player's bin has at least one stone
    # In this case all the stones in the opponent's bins go to the player's store
    if (i < (PITS + precomputed_limit) and i >= precomputed_limit and mancala_board[i] == 1 and mancala_board[TOTAL_PITS - i] > 0):
        # Collect stones from player's pit and opponent's pit and put them in player's store
        mancala_board[PITS + precomputed_limit] = mancala_board[PITS +
                                                                precomputed_limit] + (mancala_board[TOTAL_PITS - i] + 1)
        # empty player's pit and opponent's pit
        mancala_board[TOTAL_PITS - i] = mancala_board[i] = 0
        return False


# def utility(player, expectedPlayer):
#     difference = 0
#     limit1 = (PITS + 1) * player
#     limit2 = (PITS + 1) * (1 - player)
#     for i in range(0, PITS):
#         difference = difference + \
#             (mancala_board[i + limit1] - mancala_board[i + limit2])
#     return difference

def utility(expectedPlayer):
    precomputed_limit = (PITS + 1) * expectedPlayer
    for i in range(6):
        mancala_board[precomputed_limit+6] = mancala_board[precomputed_limit +
                                                           6] + mancala_board[i+precomputed_limit]

    diff = mancala_board[6] - mancala_board[13]
    if (diff < 0):
        return abs(diff), 1
    elif (diff > 0):
        return abs(diff), 0

    else:
        return abs(diff), 2


# check if game is over or not
def terminalTest():
    count = 0
    playerCounter1, playerCounter2 = 0, 0
    for pitValue in mancala_board:
        if(count == 6 or count == 13):
            continue
        if(count < 7 and pitValue == 0):
            playerCounter1 = playerCounter1 + 1
        if(count > 7 and pitValue == 0):
            playerCounter2 = playerCounter2 + 1
        count = count + 1
    if(playerCounter1 == 6):
        return True, PLAYER2
    elif(playerCounter2 == 6):
        return True, PLAYER1
    return False

# mancala_board = [0, 0, 0, 0, 0, 0, 0, 7, 7, 4, 4, 4, 4, 0]
# print(terminalTest())


# This function returns indeces of pits that have at least one stone
def actions(player):
    limit = (PITS + 1) * player
    moves = list()
    for i in range(0, PITS):
        if (mancala_board[i + limit]):
            moves.append(i)
    return moves


def print_board():
    print('############################################')
    print('P1 -->', mancala_board[0:7])
    print('P2 -->', mancala_board[7:])
    print('############################################')


# the player chooses from this list the pit number he wants to take action on
# moves = [1, 2, 3, 4, 5, 6]
# nes_moves = action(0, mancala_board)

# loop
# is human? get move #is legal movee? apply move
# else alpha beta
# alpha beta decision
# apply move

# is terminal state?(one side is empty)
# no? is free turn? (one side plays again)
# not free turn? switch player
