# 기물 움직임 파일
open_file = open('moves.txt', 'r', encoding='utf-8')
# 결과판 파일
result_file = open('result.txt', 'w', encoding='utf-8')
# 잡힌 기물 파일
out_file = open('out.txt', 'w', encoding='utf-8')

# 체스판 생성
board = [['--'] * 8 for _ in range(8)]

# 기물 세팅
for i in range(8):
    board[1][i] = 'wP'
    board[6][i] = 'bP'

pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

for i, piece in enumerate(pieces):
    board[0][i] = 'w' + piece
    board[7][i] = 'b' + piece

# line 불러오기
lines = [line.strip() for line in open_file.readlines()]

# 리스트를 읽고 알파벳을 숫자로 변경
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'a':
            lines[i] = lines[i][:j] + '1' + lines[i][j+1:]
        elif lines[i][j] == 'b':
            lines[i] = lines[i][:j] + '2' + lines[i][j+1:]
        elif lines[i][j] == 'c':
            lines[i] = lines[i][:j] + '3' + lines[i][j+1:]
        elif lines[i][j] == 'd':
            lines[i] = lines[i][:j] + '4' + lines[i][j+1:]
        elif lines[i][j] == 'e':
            lines[i] = lines[i][:j] + '5' + lines[i][j+1:]
        elif lines[i][j] == 'f':
            lines[i] = lines[i][:j] + '6' + lines[i][j+1:]
        elif lines[i][j] == 'g':
            lines[i] = lines[i][:j] + '7' + lines[i][j+1:]
        elif lines[i][j] == 'h':
            lines[i] = lines[i][:j] + '8' + lines[i][j+1:]

# lines 리스트에서 공백 삭제
lines = [line.replace(" ", "") for line in lines]

# 기물 좌표
for i in range(len(lines)):
    # 움직일 기물 좌표
    x = int(lines[i][0]) - 1
    y = int(lines[i][1]) - 1
    # 기물이 갈 좌표
    X = int(lines[i][2]) - 1
    Y = int(lines[i][3]) - 1

# 기물 잡으면 잡힌 기물 출력
    if board[Y][X] != "--":
        out_file.write(board[Y][X] + '\n')

# 기물 이동
    board[Y][X] = board[y][x]
    board[y][x] = '--'

# 결과판 출력
for i in board:
    result_file.write(' '.join(i) + '\n')

# 파일 닫기
open_file.close()
result_file.close()
out_file.close()
