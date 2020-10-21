import json
db={}

def load():
    global db
    with open('db','r',encoding='utf-8') as f:
        db=json.loads(f.read())

def dump():
    global db
    with open('db','w',encoding='utf-8') as f:
        json.dump(db,f)
