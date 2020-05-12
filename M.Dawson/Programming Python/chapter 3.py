# -*- coding: utf-8 -*-
# vk.com/nettourist
import random

class first:
    choice = random.randint(1, 3)
    if choice == 1:
        print ('Пирожок с мясом')
    if choice == 2:
        print ('Пирожок с пустотой')
    if choice == 3:
        print ('Пирожок с капустой')

class second:
    eagle = 0
    tails = 0
    counter = 0

    while True:
        throwing = random.randint(1,2)
        counter +=1

        if throwing == 1:
            print ('Reshka')
            tails += 1

        if throwing == 2:
            print ('Eagle')
            eagle += 1

        if counter == 100:
            print ('DONE')
            print ('Eagle: ' + (str(eagle)) + ', Tails: ' + (str(tails)) + (', Total throw: ' + (str(counter))))
            break

class third:
    the_number = random.randint(1,9)
    print ('Попыток 3')
    guess = int(input('Число: '))
    tries = 1

    while guess != the_number:
        if guess > the_number:
            print ('Меньше')
        if tries == 3:
            print ('STOP')
            print ('Было загадано: ' + (str(the_number)))
        else:
            print ('Больше')
        guess = int(input('Число: '))
        tries += 1

class fourth:
    number = int(input('Число: '))
    computer = 0
    tries = 1
    low = 1
    high = 100
    print(computer)

    while computer != number:
        if computer > number:
            high = computer
            computer = computer - ((high - low) // 2)
            print(computer)
        elif computer < number:
            low = computer
            computer = computer + ((high - low) // 2)
            print(computer)
        tries += 1

print("Попыток:", tries)