def connect4(stri=None):
    if stri is None:
        while True:
            try: ## user enters a number to theoretically initialize a stri x stri grid for base of the game
                stri = int(input("Enter grid size for Connect4 game: "))
                
            except ValueError:
                print("Error! try again:") ##user enters value that program unable to accept 
                continue
            if stri <= 0:
                print("Numerical error! try again:")
                continue
            break
    
    grid = [[0]*stri for _ in range(stri)]## initialize row length
    player = 1
    print("Current Board: ")
    print(*grid, sep="\n") ## print grid column step
    while True:
        user_move = retrieve_input(player, grid, stri)
        placement(user_move, player, grid)
        print("Current Board: ")
        print(*grid, sep="\n") ## print grid column step
        
        if winner(grid,player,stri) or winner(zip(*grid),player,stri) or diag_won(grid[::-1], player, stri) or diag_won(grid, player, stri):
            print("Congratulations, {0} player has won".format(player))
            return
        if not any(0 in gri for gri in grid):
            return
        player = 2 if player == 1 else 1
   
def retrieve_input(player, grid, stri):## retrieve numerical input value 
    playerinstruct = "Enter a key from {0} to {1} player {2}:".format(1,stri,player)
    while True:## infinite loop until return is executed
        try:
            user_data = int(input(playerinstruct))
        except ValueError:## is it even a number?
            print("Error Value {0} doesn't work".format(user_data))
            continue
        if 0 >  user_data or user_data > stri+1:## check if input within grid
            print("Error Value {0} doesn't work".format(user_data))
        elif grid[0][user_data - 1] != 0:## check is spot already filled
            print("piece already exists here")
        else:## return user data - 1 because list placement starts at 0
            ans = user_data - 1
            return ans


def diag_won(grid, player, stri):## check both diagonals
    return all(any(grid[g][g] == player for g in range(stri)))
     
def winner(grid, player, stri):## check for if any of colums or rows are all from one player
    return any(all(e == player for e in gri)for gri in grid)

def placement(user_move, player, grid):## function that puts player piece into grid
    for gri in grid[::-1]:
        if not gri[user_move]:
            gri[user_move] = player
            return



if __name__ == '__main__':
    connect4()
    


    
    

            
            
            
            
            
    
    
    
                
                