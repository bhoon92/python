#후보자 10명, 학생 10명, 기권 없음, 투표권 각 1장, 최다 투표, 반장

def vote(list):
    for i in range(0, len(list)):
        list [i] = int(list[i])


def countVotes(votes):
    earns = [0,0,0,0,0,0,0,0,0,0]
    for v in votes :
        earns[v-1] += 1
    return earns

def maxVote(list):    
    max = 0
    maxIdx=0
    i=0

    for num in list :
        if num > max :
            max = num
            maxIdx = i
        i+=1
    return maxIdx

def printEarns(earns):
    for i in range(0, len(earns)):
        print("기호 : ", i+1, "득표수 : ", earns[i])


#투표 시작
votes = input("투표할 후보의 번호를 space구분으로 10번 입력하세요.").split()
vote(votes)
earns = countVotes(votes)
winner = maxVote
printEarns(earns)
print("최다득표자 : ",winner)