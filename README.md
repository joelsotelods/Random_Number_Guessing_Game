# Random Number Guessing Game

I created this program for education purposes only.. 
I come from a c/c++ background and I started learning Python a week ago.. so I saw this programming challenge in a course I'm taking..

This is a Game about guessing a random number: Basically the program generates a random number internally between 1 and 100 and it asks you for an integer.

Rules:
 * To exit the program without finishing it, you should enter 0.
 * If you input something anything different than an int.. the program will ask you for an int.
 * If you input a number lower than 1 (negatives) or higher than 100 the program will tell you that the number is out of range.
 
Messages in the first guess:
  * If the number entered is in a range of 10 in the first guess, the program will tell you that you are warm!
  * If in the first guess you are out of range, the program will tell you that you are cold!
 
In the following guesses.. the program will compare the last guessed number and the new guessed number and will tell you if you are getting closer to the number or you are getting "colder!"

At the end, when you find out the number.. the program wiil tell you the number of tryes that you did.

```

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

```


