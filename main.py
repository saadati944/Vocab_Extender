import db

db.load()

while True:
    for w in db.getnewword(int(input('count : '))):
        print(w)
    print()
    print()