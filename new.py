# returns the board after making a move
def play(board, block_no, player, mode):
    store_flag = 0
    # 2nd player playing
    block_no = block_no - 1
    if (player):
        block_no = block_no+7
        for i in range(board[block_no]):
            if ((block_no + i + 1) % 14 == 6):
                board[(block_no + i + 2) %
                      14] = board[(block_no + i + 2) % 14] + 1
                store_flag = 1
            else:
                board[(block_no + i + 1 + store_flag) %
                      14] = board[(block_no + i + 1 + store_flag) % 14] + 1
        # stealing
        if(mode and (board[(block_no + i + 1 + store_flag) % 14] == 1) and ((block_no + i + 1 + store_flag) % 14 > 6)):
            board[13] = board[13] + 1 + \
                board[(12-((block_no + i + store_flag) % 14))]
            board[(block_no + i + 1 + store_flag) % 14] = 0
            board[(12-((block_no + i + store_flag) % 14))] = 0
    # 1st player playing
    else:
        for i in range(board[block_no]):
            if ((block_no + i + 1) % 14 == 13):
                board[(block_no + i + 2) %
                      14] = board[(block_no + i + 2) % 14] + 1
                store_flag = 1
            else:
                board[(block_no + i + 1 + store_flag) %
                      14] = board[(block_no + i + 1 + store_flag) % 14] + 1
        # stealing
        if(mode and (board[(block_no + i + 1 + store_flag) % 14] == 1) and ((block_no + i + 1 + store_flag) % 14 < 6)):
            board[6] = board[6] + 1 + \
                board[(12-((block_no + i + 1 + store_flag) % 14))]
            board[(12-((block_no + i + 1 + store_flag) % 14))] = 0
            board[(block_no + i + 1 + store_flag) % 14] = 0
    board[block_no] = 0

    return board

# when one side has no more moves (empty side in the board)
# this function returns the score (diff between the 2 stores and the winner)
# takes the player whose side of the board is non empty


def calc_score(board, player):
    player2_flag = 0
    if (player):
        player2_flag = 7

    for i in range(6):
        board[player2_flag+6] = board[player2_flag+6] + board[i+player2_flag]
    diff = board[6] - board[13]
    if (diff < 0):
        return abs(diff), 1
    elif (diff > 0):
        return abs(diff), 0
    else:
        return abs(diff), 2

# board = [0,1,3,2,3,2,3  , 2,2,0,1,2,2,0]
# print(play(board, block_no  =6, player=1, mode=1))
# board = [1,1,3,0,0,0,0  , 0,0,0,0,0,0,10]
# print(calc_score(board,0))

# The game is over when one player’s pits are completely empty.
def isGameOver(board):
    if (any(board[0:6]) != 0 and any(board[7:13]) != 0):
        return False
    return True

# board = [0, 0, 0, 0, 0, 0, 15,
#          0, 0, 2, 0, 0, 0, 10]
# print(isGameOver(board))

def heurestic1(player, board):
    return board[6 + (7) * player] - board[6 + (7) * (1 - player)]


# Number of stones on player's board with decreasing probability from 0 - 5
# This heuristic gives more weight to the stones on the far left of the player's store
def heuristic3(player, board):
    count = 0
    limit1 = (7) * player
    for i in range(6):
        count = count + 0.1 * (6 - i) * \
            (board[i + limit1])
    return count

def evaluation(player,board):
        return heurestic1(player,board) + heuristic3(player, board)

def noOfNonEmptyPits(board, player):
    moves = []
    limit = 7 * player
    for i in range(6):
        if(board[i+limit]):
            moves.append(i)
    return moves
