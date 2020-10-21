import json,os
db={}
rdb={}

def load():
    global db,rdb
    with open('db','r',encoding='utf-8') as f:
        db=json.loads(f.read())
    if not os.path.exists('rdb'):
        generateRDB()
    else:
        with open('rdb','r',encoding='utf-8') as f:
            rdb=json.loads(f.read())

def dump():
    global rdb
    with open('rdb','w',encoding='utf-8') as f:
        json.dump(rdb,f)

def generateRDB():
    global db,rdb
    for k in db.keys():
        #v=views count , d=difficulty
        rdb[k]={'v':0,'d':0}


if __name__=='__main__':
    load()
    dump()
