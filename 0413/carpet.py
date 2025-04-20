# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    total = brown + yellow

    for width in range(3, total + 1):
        if total % width == 0:
            height = total // width
            if width >= height and (width - 2) * (height - 2) == yellow:
                return [width, height]

# def solution(brown, yellow):
#     total = brown + yellow
#     possible_sizes = []
#
#     for width in range(1, total + 1):
#         if total % width == 0:
#             height = total // width
#             if width >= height:
#                 possible_sizes.append((width, height))
#
#     return list(possible_sizes[-1])