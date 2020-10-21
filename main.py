import db, config
from os import system,name

def clear():
    _= system('cls' if name=='nt' else 'clear')

db.load()

def discover(count=config.words_in_each_discover):
    words=db.getnewword(count)
    i=1
    for w in words:
        clear()
        print(f"{i} :   {w}")
        print("\n",db.db[w])
        db.view(w)
        input('\npress enter to continue...')
        i+=1

def practice(count=config.words_in_each_practice):
    words=db.getpractice(count)
    if len(words)==0:
        input(config.message_for_ending_practicing)
    i=1
    for w in words:
        clear()
        print(f"{i} :   {w}")
        print("\n",db.db[w])
        db.view(w)
        input('\npress enter to continue...')
        i+=1


while True:
    discover()
    practice()
