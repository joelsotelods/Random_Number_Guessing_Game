
import random
randomnum = random.randint(0,100)

print('hello: this is the guessing game.. please introduce a number and I''try to guess it ')

a = [0]
val = 0

distance = 100
while True:

    text = input('Enter  a number here (1 to 100) (Exit=0): ')
    
    try:
        val = int(text)
    except ValueError:
        print("That's not an int!")
        continue
    
    a.append(val)
    #print(a[-1])
    
    if a[-1] == 0:
        print('bye')
        break
    
    distance = abs(a[-1]-randomnum)
    
    if a[-1]<1 or a[-1]>100:
        print('out of bounds bru!.. it should be between 1 and 100')

    elif distance == 0:
        print('WINNER!! You made it in {} tryes.'.format(len(a)-1))
        break
        
    elif a[-2] == 0:
        if distance>5:
            print('COLD!')
        elif distance<=5:
            print('WARM!')
        else:
            print('WFT! error')

    elif a[-2] != 0:
        if abs(a[-1]-randomnum)>abs(a[-2]-randomnum):
            print('COLDer!')
        elif abs(a[-1]-randomnum)<abs(a[-2]-randomnum):
            print('WARMer!')
        elif abs(a[-1]-randomnum)==abs(a[-2]-randomnum):
            print('Seriously?!')
        else:
            print('WFT! error')
    
exit()
