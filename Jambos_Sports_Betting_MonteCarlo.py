import random
import matplotlib
import matplotlib.pyplot as plt


initial_funds = 45000
cost = 3000
# return of rolling a dice that can come up at 1 to 100, with simple win/loss
def bet_odds():
    roll = random.randint(1,100)
    
    if roll <= 45:   
        # if roll is less than or equal to 44 you lose   
        return False
    elif 100 >= roll > 45:
        # if roll is greater than 45
        # only a 5% edge. Fifty-five percent chance of winning each bet 
        return True
        
''' 
Simple bettor, betting the same amount each time.
'''
exp = []

def simple_bettor(funds, initial_wager, wager_count):
    global broke_count
    global loss_count
    value = funds
    wager = initial_wager
    
    #wager X
    wX = []
    #value Y
    vY = []
    
    #change to 1, to avoid confusion so we start at wager 1   
    currentWager = 1
    
    # change to less than or equal
    while currentWager <= wager_count:
        if bet_odds():
            value += wager
            # append
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            # append
            wX.append(currentWager)
            vY.append(value)
            if value < 0:
                broke_count += 1
                break
            
        currentWager += 1
    if value < 45000:
        loss_count += 1
    
    if value > 60000:
        exp.append(value)
            
    plt.plot(wX,vY)
    
    
x = 0
broke_count = 0
loss_count = 0
 

# Now I can play around with these numbers to change the amount of bettors, bets, and value of bets.
while x < 1000:
    simple_bettor(55000, 700, 1200)       
    x += 1

print('death rate:', (broke_count/float(x))*100)
print('survival rate:',100 - ((broke_count/float(x))*100))                
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.axhline(45000, color = 'r')
plt.show()

print('unrecoverable loss:',(loss_count/float(x))*100)
print('profitable:',100 - ((loss_count/float(x))*100))

print('expected profit:', (round((sum(exp)/len(exp)) - (initial_funds + cost), 2)))