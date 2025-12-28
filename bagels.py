import random



num_of_digits=3
max_trials=10


def main():

    while True:
        secret=getSecretnum()
        num_of_attemps = 0
        while num_of_attemps<max_trials:
            guess=''
            while len(guess) !=num_of_digits:
                guess=input('guess :')
            num_of_attemps +=1
            clues=getClues(guess,secret)
            print(clues)
            if guess==secret:
                print('congrates you won')
                break
            if num_of_attemps==max_trials:
                print(f'secret num is {secret}\n you lost')
        break


def getSecretnum():
    numbers=list('0123456789')
    random.shuffle(numbers)
    secret=''
    for i in range(num_of_digits):
        secret +=numbers[i]
    return secret
def getClues(guess,secret):
    if guess==secret:
        return ('wow ! I am so proud of you')
    clues=[]
    for i in range(len(guess)):
     if guess[i]==secret[i]:
         clues.append('fermi')
     elif guess[i] in secret:
         clues.append('pico')
    if not clues:
        return ('bagels')
    else:
        clues.sort()
        return''.join(clues)

if __name__=="__main__":
    main()



