import datetime
import random
from  calendar import month_name




def getBirthday(numberOfBirthdays):
    birthdays=[]
    start0fYear=datetime.date(2025,1,1)
    for i in range(numberOfBirthdays):
        randomNumOfDays=datetime.timedelta(random.randint(1,364))
        birthday=start0fYear+randomNumOfDays
        birthdays.append(birthday)
    return birthday
def getMatch(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    for a , birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if a!=b and birthdayA==birthdayB:
                return birthdayA
print("""
The Birthday Paradox shows us that in a group of N people,
the odds that two have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random 
simulations) to explore this concept.
""")
Months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
          'Sep','Oct','Nov','Dec')

while True:
    response=input('choose a number from 1 to 100')
    if response.isdecimal() and (0<int(response<=100)):
        numBDays=int(reponse)
        break
print()
print(f'here are,{numBDays} birthdays ')
birthdays=getBirthday(numBDays)
for i,birthday in enumerate(birthdays):
    print(',',end='')
    monthName=Month[birthday.month()-1]
    dateText=(f'{monthName},{birthday.day}')
    print(dateText,end='')

print('\n')
match=getMatch(birthdays)
if match is not None:
    monthName=Months[match.months-1]
    dateText=(f'{monthName},{match.day}')
    print(f'many people have a birthday on {dateText}')
else:
    print('There are no matching birthdays')

print()
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')
print("Let's run another 100,000 simulations.\n")

simMatch=0
for i in range(100000):
    if i %100000 ==0:
        print(i,'simulation runs')
    birthdays=getBirthday(numBDays)
    if getMatch(birthdays) is not None:
        simMatch +=1
probability=round(simMatch/100000*100,2)

print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print("That's probably more than you would think!")



