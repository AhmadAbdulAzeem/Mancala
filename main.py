
PITS=6
TOTAL_PITS = 12
def action(player, mancala_board):
    moves=[]
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
    while (stones) :
            i = (i + 1) % BOARD_SIZE

            if (i == opponent_store):
                 continue
            mancala_board[i]= mancala_board[i]+1
            stones= stones -1


mancala_board = [6,6,6,4,0,4,0,7,7,4,4,4,4,0] #stones per pit
moves = [1,2,3,4,5,6]  #the player chooses from this list the pit number he wants to take action on
nes_moves =action(0, mancala_board)

#loop
#is human? get move #is legal movee? apply move
#else alpha beta
    #alpha beta decision
    #apply move

#is terminal state?(one side is empty)
    #no? is free turn? (one side plays again)
    #not free turn? switch player