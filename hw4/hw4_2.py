import random
card = []
player = []
dealer = []
color = {0:'SPADE',1:'HEART',2:'DIAMOND',3:'CLUB'}
num = {1:'ACE',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'JACK',12:'QUEEN',13:'KING'}
value = {1:11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:10,12:10,13:10}
cur = 0
dealer_value = 0
player_value = 0
dealer_ace_flag = 0
player_ace_flag = 0
for i in range(1,53):
    card.append(i)

def printplayercard():
    global player_value,player_ace_flag
    if(player_value == 21):
        print('Your current value is Blackjack! (21)')
    elif(player_value > 21):
        if(player_ace_flag > 0):
            player_value -= 10
            player_ace_flag -= 1
            print('Your current value is',player_value)
        else:
            print('Your current value is Bust! (>21)')
    else:
        print('Your current value is',player_value)
    global player
    n = len(player)
    print('with the hand:',end = ' ')
    for i in range(n):
        s = num[(player[i] % 13) + 1] + '-' + color[player[i] % 4]
        if(i == n - 1):
            print(s)
        else:
            print(s,end = ', ')
    print('')

def printdealercard():
    global dealer_value,dealer_ace_flag
    if(dealer_value == 21):
        print('Dealer\'s current value is Blackjack! (21)')
    elif(dealer_value > 21):
        if(dealer_ace_flag > 0):
            dealer_ace_flag -= 1
            dealer_value -= 10
            print('Dealer\'s current value is',dealer_value)
        else:
            print('Dealer\'s current value is Bust! (>21)')
    else:
        print('Dealer\'s current value is',dealer_value)
    global dealer
    n = len(dealer)
    print('with the hand:',end = ' ')
    for i in range(n):
        s = num[(dealer[i] % 13) + 1] + '-' + color[dealer[i] % 4]
        if(i == n - 1):
            print(s)
        else:
            print(s,end = ', ')
    print('')

def startgame():
    random.shuffle(card)
    global player,dealer
    global cur,player_value,dealer_value,player_ace_flag,dealer_ace_flag
    dealer_ace_flag = 0
    player_ace_flag = 0
    player = []
    dealer = []
    cur = 4
    player.append(card[0])
    player.append(card[1])
    player_value = value[card[0] % 13 + 1] + value[card[1] % 13 + 1]
    dealer.append(card[2])
    dealer.append(card[3])
    dealer_value = value[card[2] % 13 + 1] + value[card[3] % 13 + 1]
    printplayercard()

def dealer_time():
    global cur
    global dealer_value,player_value
    global card
    printdealercard()
    while(dealer_value < 17):
        s = num[(card[cur] % 13) + 1] + '-' + color[card[cur] % 4]
        print('Dealer draws',s)
        print('')
        dealer.append(card[cur])
        dealer_value += value[card[cur] % 13 + 1]
        cur = cur + 1
    printdealercard()

def endgame():
    if(dealer_value > 21):
        print('*** You beat the dealer! ***')
        print('')
    elif(dealer_value == player_value):
        print('*** Your tied the dealer, nobody wins. ***')
        print('')
    else:
        print('*** Dealer wins! ***')
        print('')
    
startgame()
while(1):
    op = int(input('Hit or stay? (Hit = 1, Stay = 0): '))
    print('')
    if(op == 1):
        s = num[(card[cur] % 13) + 1] + '-' + color[card[cur] % 4]
        player.append(card[cur])
        player_value += value[card[cur] % 13 + 1]
        print('You draw',s)
        print('')
        printplayercard()
        cur = cur + 1
        if(player_value > 21):
            op2 = str(input('Want to player again? (y/n): '))
            if(op2 == 'y'):
                print('')
                print('-----------------------')
                print('')
                startgame()
                continue
            else:
                break
    else:
        dealer_time()
        op2 = ''
        endgame()
        op2 = str(input('Want to player again? (y/n): '))
        if(op2 == 'y'):
            print('')
            print('-----------------------')
            print('')
            startgame()
            continue
        else:
            break
