import pickle
import os
filepath = 'score.bin'
def input_scores() :
    scores = []
    n = 1
    score = 0
    while score >= 0 :
        score = int(input(f'#{n}? '))
        if score < 0 :
            return scores
        
        scores.append(score)
        n += 1

def get_average(lst) :
    n = 0
    for i in lst :
        n += i
    n = n / len(lst)
    return n
def show_scores(lst) :
    for i in lst :
        print(i,end = ' ')
    print()
def save_data(lst) :
    with open(filepath,'wb') as file :
        pickle.dump(lst,file)
def load_data() :
    with open(filepath,'rb') as file :
        scores = pickle.load(file)
        return scores
if os.path.exists(filepath) :
    print('[파일 읽기]')
    print()
    print('[점수 출력]')
    scores = load_data()
    print('점수 출력 : ',end = '')
    show_scores(scores)
    print(f'평균 : {get_average(scores)}')
else :
    print('[점수 입력]')
    scores = input_scores()
    print()
    print('[점수 출력]')
    print('점수 출력 : ',end = '')
    show_scores(scores)
    print(f'평균 : {get_average(scores)}')
    save_data(scores)

