# r : read only
# r+ : read & write
file = open('read.txt', 'r', encoding='utf-8')

# read - 전체 파일 읽기
read = file.read()
print('read()', read)

file.close()

file = open('read.txt', 'r', encoding='utf-8')

# read line - 라인 한 줄씩 읽기
line1 = file.readline()
line2 = file.readline()
print('readline()', line1, line2)

file.close()

file = open('read.txt', 'r', encoding='utf-8')

# read lines - 모든 라인을 배열로 읽어옴
lines = file.readlines()
print('readlines()', lines)

file.close()
