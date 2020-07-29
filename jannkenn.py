import random


com = True
while(com):
    player = int(input('0:グー、1:パー、2:チョキ'))
    enemy = random.randint(0,2)
    if player == enemy:
        print('引き分け')
    elif player == 0 and enemy == 1:
        print('負け')
    elif player == 1 and enemy == 2:
        print('負け')
    elif player == 2 and enemy == 0:
        print('負け') 
    else:
        print('勝ち')
    aaa = int(input('4:終了'))
    if aaa == 4:
        com = False
   
