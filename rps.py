def rps(p1,p2):
    if p1 == 'rock' and p2 == 'scissors':
        return 'player 1 won!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'player 1 won!' 
    elif p1 == 'paper' and p2 == 'rock':
        return 'player 1 won!'
    
    elif p1 == 'scissors' and p2 == 'rock':
        return 'player 2 won!'
    elif p1 == 'paper' and p2 == 'scissors':
        return 'player 2 won!'
    elif p1 == 'rock' and p2 == 'paper':
        return 'player 2 won!'
        
    else:
        return ('Draw!')


print (rps('rock','scissors'))
print (rps('scissors', 'paper'))
print (rps('paper', 'rock'))

print (rps('scissors', 'rock'))
print (rps('paper', 'scissors'))
print (rps('rock', 'paper'))

print (rps('rock', 'rock'))
print (rps('scissors', 'scissors'))
print (rps('paper', 'paper'))


