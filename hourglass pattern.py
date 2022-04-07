for i in range(5):
    for j in range(i):
        print(' ',end='')
    for k in range(5-i):
        print('*',end=' ')
    print('\n')
for i in range(4,0,-1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(i,6):
        print('*',end=' ')
    print('\n')