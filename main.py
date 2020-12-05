import db
import config
from os import system, name
import random
import time


def clear():
    _ = system('cls' if name == 'nt' else 'clear')


def discover(count=config.words_in_each_discover):
    words = db.getnewword(count)
    if len(words) == 0:
        input(config.message_for_ending_discover)
        return
    i = 1
    for w in words:
        clear()
        print(config.discover_header)
        print(f"{i} : {w}")
        print("\n", db.db[w])
        db.view(w)
        input('\npress enter to continue...')
        i += 1


def practise(count=config.words_in_each_practise):
    words = db.getpractise(count)
    if len(words) == 0:
        input(config.message_for_ending_practicing)
        return
    i = 1
    for w in words:
        clear()
        print(config.practise_header)
        print(f"{i} : {w}")
        print("\n", db.db[w])
        db.view(w)
        input('\npress enter to continue...')
        i += 1


def question(word):
    print(config.question_text_before, word,
          config.question_text_after, sep='', end='\n\n')
    correctans = random.randint(1, 4)
    wrongans = []
    for i in range(1, 5):
        if i == correctans:
            print('\t', i, ') ', db.db[word], sep='', end='\n\n')
        else:
            wr = random.randint(0, len(db.words)-1)
            while wr in wrongans:
                wr = random.randint(0, len(db.words)-1)
            wrongans.append(wr)
            print('\t', i, ') ', db.db[db.words[wr]], sep='', end='\n\n')
    ans = 0
    while ans not in ['1', '2', '3', '4']:
        ans = input('enter correct answer (1, 2, 3, 4) : ')
    if ans == str(correctans):
        db.difficult(word, False)
        return True
    else:
        db.difficult(word, True)
        return False


def test(count=config.words_in_each_test):
    words = db.gettest(count)
    if len(words) == 0:
        input(config.message_for_ending_test)
        return
    score = 0
    i = 1
    for w in words:
        clear()
        print(config.test_header)
        print(i, ': ', end='')
        if question(w):
            score += 1
        i += 1
    clear()
    print('your score is :', score, 'out of', count)
    with open(config.scores_log_file_name, 'a', encoding='utf-8') as f:
        f.write('%s - %d/%d\n' % (time.asctime(), score, count))
    input('press enter to continue...')


def showstats():
    clear()
    # returned list : [total,discovered,not_practised_words,fully_practised_words,fully_tested_words]
    res = db.countwords()
    print('total words :', res[0])
    print('discovered words :', res[1])
    print('not practised words :', res[2])
    print('fully practised words :', res[3])
    print('fully tested words :', res[4])
    input('\n\npress enter to continue...')


def main():
    while True:
        clear()
        print(config.menu)
        ans = input(config.menu_question).lower()
        if ans == 'e':
            db.dump()
            exit()
        elif ans == 'd':
            discover()
        elif ans == 'p':
            practise()
        elif ans == 't':
            test()
        elif ans == 's':
            showstats()


if __name__ == '__main__':
    db.load()
    db.shuffle()
    main()
