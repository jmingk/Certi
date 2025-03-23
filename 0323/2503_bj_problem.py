# https://www.acmicpc.net/problem/2503

import sys
from itertools import permutations
sys.stdin = open('2503_input.txt', 'r')

# case = int(input())

possible_numbers = list(permutations(range(1, 10), 3))

def check_guess(guess, answer, strike, ball):
    guess_strike = 0
    guess_ball = 0

    for i in range(3):
        if guess[i] == answer[i]:
            guess_strike += 1
        elif guess[i] in answer:
            guess_ball += 1

    return guess_strike == strike and guess_ball == ball

case = int(input())

answer_num = []
guess = []
for i in range(case):
    answer_num.append(list(map(int, input().split())))
    str_num = str(answer_num[i][0])
    list(str_num)
    int_list = list(map(int, str_num))
    guess.append([int_list, answer_num[i][1], answer_num[i][2]])
#print(guess)

for answer, strike, ball in guess:

    filtered_numbers = []
    for num in possible_numbers:
        if check_guess(num, answer, strike, ball):
            filtered_numbers.append(num)
    possible_numbers = filtered_numbers

print(len(possible_numbers))

#
# strike_list = []
# check_list = []
# def baseball_game(strike, ball, a):
#     print(a)
#     print(strike)
#     print(ball)
#     for _ in range(3):
#
#     return
#
# answer = []
# guess = []
# for i in range(case):
#     answer.append(list(map(int, input().split())))
#     str_num = str(answer[i][0])
#     list(str_num)
#     int_list = list(map(int, str_num))
#     guess.append(int_list)
#
#
# for j in range(case):
#     baseball_game(answer[j][1],answer[j][2],guess[j])