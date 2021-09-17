board={'1':' ','2':' ','3':' ',
       '4':' ','5':' ','6':' ',
       '7':' ','8':' ','9':' '}
def tictac():
    count=0
    place='X'
    player=player_1
    for i in range(10):
        print(player,"enter your position to place",place,"!!")
        n=input()

        if (board[n] == ' '):
            count=count+1
            board[n]=place
            print_board()
        else:
            print("This position is already filled!!")
            print_board()
            continue
        if count>=5:
            if board['1'] == board['2'] == board['3'] != ' ': # across the top
                print_board()
                print("\nGame Over.\n")                
                print(" **** " + player + " won ****")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
                print_board()
                print("\nGame Over.\n")                
                print(" **** " +player+ " won. ****")
                break
            elif board['7'] == board['8'] == board['9'] != ' ': # across the bottom
                print_board()
                print("\nGame Over.\n")                
                print(" **** " +player+ " won. ****")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                print_board()
                print("\nGame Over.\n")                
                print(" **** " +player+ " won. ****")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                print_board()
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                print_board()
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
                print_board()
                
                print("\nGame Over.\n")                
                print(" **** " +player+ " won. ****")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                print_board()
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break 
        if count>=9:
            print("Tie !!")
        if place=='X' and player==player_1:
            place='O'
            player=player_2
        else:
            place='X'
            player=player_1
            
        
    start=input("wanna play again !!! then enter 1 else enter 0 : ")
    if start==1:
        tictac()
def print_board():
    print(board['1'] ,'|',board['2'],'|',board['3'])
    print("-+--+-")
    print(board['4'],'|',board['5'],'|',board['6'])
    print("-+--+-")
    print(board['7'],'|',board['8'],'|',board['9'])
player_1=input("Player1 ! enter your name : ")
player_2=input("Player2 ! enter your name: ")
print(player_1," yours symbol is ","X")
print(player_2,"yours symbol is ","O")
print_board()
tictac()


    
    
    
    
    
