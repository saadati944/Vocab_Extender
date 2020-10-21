import db, config
from os import system,name
import random

def clear():
    _= system('cls' if name=='nt' else 'clear')

db.load()

def discover(count=config.words_in_each_discover):
    words=db.getnewword(count)
    if len(words)==0:
        input(config.message_for_ending_discover)
        return
    i=1
    for w in words:
        clear()
        print(f"{i} : {w}")
        print("\n",db.db[w])
        db.view(w)
        input('\npress enter to continue...')
        i+=1

def practise(count=config.words_in_each_practise):
    words=db.getpractise(count)
    if len(words)==0:
        input(config.message_for_ending_practicing)
        return
    i=1
    for w in words:
        clear()
        print(f"{i} : {w}")
        print("\n",db.db[w])
        db.view(w)
        input('\npress enter to continue...')
        i+=1

def question(word):
    print(config.question_text_before,word,config.question_text_after,sep='',end='\n\n')
    correctans=random.randint(1,4)
    wrongans=[]
    for i in range(1,5):
        if i==correctans:
            print(i,') ',db.db[word],sep='',end='\n\n')
        else :
            wr=random.randint(0,len(db.words)-1)
            while wr in wrongans:
                wr=random.randint(0,len(db.words)-1)
            wrongans.append(wr)
            print(i,') ',db.db[db.words[wr]],sep='',end='\n\n')
    ans=0
    while ans not in ['1','2','3','4']:
        ans=input('enter correct answer (1, 2, 3, 4) : ')
    return ans==str(correctans)

def test(count=config.words_in_each_test):
    words=db.gettest(count)
    if len(words)==0:
        input(config.message_for_ending_test)
        return
    score=0
    i=1
    for w in words:
        clear()
        print(i,': ',end='')
        if question(w):
            score+=1
        i+=1
    clear()
    print('your score is :',score)
    input('press enter to continue...')

while True:
    test()
    practise()
    discover()
    db.dump()
