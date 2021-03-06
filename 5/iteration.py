arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())  # n 행,m 열
arr = [list(map(int, input().split())) for _ in range(n)] #list 값 입력


def solve():
    sum = 0
    while True:
        move = True
        for i in range(0, n):
            for j in range(0, m):
                if arr[i][j] == 0:
                    continue
                cnt = 0
                current = arr[i][j]
                for k in range(0, 4):
                    nx = i + dx[k]  #다음 좌표의 행
                    ny = j + dy[k]  #다음 좌표의 열
                    if nx < 0 or nx >= m or ny < 0 or ny >= n: #탐색이 범위를 벗어나면 break
                        break

                    if arr[nx][ny] < current: #탐색 좌표 연못깊이가 현재 연못 깊이보다 얕으면 break
                        break
                    cnt += 1

                if cnt == 4:    #상하좌우 연못 깊이가 현위치보다 깊거나 같으면 현위치에서 1을 더함
                    arr[i][j] += 1
                    move = False

        if move:
            break

        for i in range(0, n):
            for j in range(0, m):
                if arr[i][j] == 0:
                    continue
                sum += arr[i][j]
    print(arr)
    print(sum)


if __name__ == '__main__':
    solve()
