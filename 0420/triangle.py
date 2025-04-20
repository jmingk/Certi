def solution(triangle):
    row_count = len(triangle)

    for i in range(1, row_count):
        column_count = len(triangle[i])

        for j in range(column_count):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == column_count - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    last_row = triangle[row_count - 1]
    return max(last_row)
