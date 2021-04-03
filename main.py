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


MAX_QSIZE = 100


class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]


def solution13(priorities, location):
    cq = CircularQueue()
    max_priorities = max(priorities)
    cq.enqueue(priorities)
    # print(max_priorities)
    # for i in range(len(priorities)):
    # CircularQueue.enqueue(priorities)
    # print("나야" + dic) ㅋㅋㅋㅋㅋ엥 왜 .//.....얼탱방구네

    # print(0)
    return 0


# solution17
a, b = map(int, input().strip().split(' '))
l = ["*" for i in range(a)]
for k in range(b):
    print(''.join(l))
print(a + b)
answer = ('*'*a +'\n')*b
print(answer)


def solsol(n):
    return 'Even' if n % 2 == 0 else 'Odd'


def solution_l2_3(prices):
    answer3 = []
    return answer3



class PJB:
    def solution42587(self, priorities, location):
        priority_set = list(set(priorities))
        priority_set.sort(reverse=True)

        cnt = 0

        for priority in priority_set:
            print(f"current priority: {priority}")

            for i in range(0, len(priorities)):
                print(f"current: {i} {priorities[i]}")
                if priority <= priorities[i]:
                    print("istrue")
                    cnt += 1
                if priority != priorities[i]:
                    continue
                if location == i:
                    return cnt


def test42587(function):
    priorities = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1]]
    location = [2, 0]
    result = []
    for i in range(0, 2):
        print(f"TestCase {i} input: {priorities[i]} {location[i]}")
        print(function(priorities[i], location[i]))


print(solution_l2_3([1, 2, 3, 2, 3]))

# test42587(solution13)
#test42587(PJB().solution42587)

# https://programmers.co.kr/learn/courses/30/lessons/42587
