import random
answer = random. randint (0, 100)
print ('choose a number between 0 and 100.')
count = 0
min = 0
max = 100
while True:
    count = count + 1
    print ('\nyou have attempted at guessing the correct number {} time/s.'. format (count))
    user = int (input ('what is your guess? ({}-{}) '. format (min, max)))
    if user == -1:
        print ('\nyou have failed in guessing the number. the answer was {}.'. format (answer))
        break
    elif user > answer:
        print ('\nyour guess is bigger than the answer.')
        max = user - 1
    elif user < answer:
        print ('\nyour guess is smaller than the answer.')
        min = user + 1
    elif user == answer:
        print ('\nyour answer is correct!')
        break
