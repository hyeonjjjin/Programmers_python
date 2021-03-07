import math


def solution10(n):
    answer = 0
    index = [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]
    for i in index:
        m, n = divmod(n, i)
        answer += m
    return answer


def solution11(n):
    return list(map(int, list((str(n))[::-1])))


def solution12(n):
    # x=1-7071067
    if int(math.sqrt(n)) == math.sqrt(n):
        return (int)(math.sqrt(n) + 1) ** 2
    else:
        return -1


class PJB:
    def solution12(n):
        return solution12(n)


# 디스이즈 날먹이자식ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ파이썬에서 class 처으모바 3점 획득 !
# 나도파이썬안써서 잘몰라ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅎ통과??오롤ㄹ롤ㄹ다음문제!깃에 올려야돼1!!!!
# 오저게 뭔답이야야답무ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 어뭐야**되냐야뭐어ㅇ
# 엇 습관적인 컨트롤제트 오늘 푸시 많이해서 앞에 커밋한거 색 연해졌어,, 앞에 연약해져서 맘에 안들아,, 오오오겁나찐해오올올 밑에 터미널일케해두되는거니
# 케는중이이는느 난 안해봤는데 너 하길래 구거ㅕㅇ함ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ나
# ㅋㅋㅋㅋㅋㅋㅋ

print(solution11(12345))
print(solution12(3))
