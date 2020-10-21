import json, os, random
import config

db={}
words=[]
rdb={}

def load():
    global db,rdb
    with open('db','r',encoding='utf-8') as f:
        db=json.loads(f.read())
    for k in db.keys():
        words.append(k)
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
    for k in words:
        #v=views count , d=difficulty
        rdb[k]={'v':0,'d':0}

def getnewword(count):
    global rdb,words
    l=[]
    for k in  words:
        if rdb[k]['v']==0:
            l.append(k)
        if len(l)==count:
            return l
    return l
def getpractice(count):
    global rdb,words
    l=[]
    for k in  words:
        if rdb[k]['v']>0 and rdb[k]['v']<=config.max_practices_for_each_word:
            l.append(k)
        if len(l)==count:
            return l
    return l

def gettest(count):
    global rdb,words
    l=[]
    for k in  words:
        if rdb[k]['v']>0 :
            l.append(k)
    if count>len(l):
        count=len(l)
    ws=[]
    for i in range(count):
        ws.append(l.pop(random.randint(0,len(l)-1)))
    return ws

def view(word):
    rdb[word]['v']+=1

def difficult(word,moredifficult=True):
    if moredifficult:
        rdb[word]['d']+=1
    else:
        rdb[word]['d']-=1

if __name__=='__main__':
    load()
    dump()
    print('all done...')
    input('press enter to continue ...')
