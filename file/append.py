# a : append only
# a+ : read & append
file = open('append.txt', 'a', encoding='utf-8')
file.write('additional text')
