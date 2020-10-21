import db
from os import system,name

def clear():
    _= system('cls' if name=='nt' else 'clear')

db.load()

def discover(count=5):
    words=db.getnewword(count,True)
    i=1
    for w in words:
        clear()
        print(f"{i} :   {w}")
        print("\n",db.db[w])
        input('\npress enter to continue...')
        i+=1



while True:
    discover()
