import deck

game = 0 
totalRounds = 0

while game is 0:
    numRounds = 0
    bankroll = int(input("Enter initial amount: "))
    win = bankroll *2
    simulate = 0
    gameOn = 0
    count = 0
    
    while simulate is 0:
        totalRounds += deck.totalRounds(bankroll)
        count = count + 1
        if count is 100:
            simulate = 1

    print ("Average number of rounds: " + str("{:.3f}".format(totalRounds*1.000/100.000)))
    response = input("Enter 0 to exit. ")
    print("\n")
    if response is "0":
        game = 1

    totalRounds = 0
    
    
        
   

    


