in_arr = [int(i) for i in input().split()]
out_arr = []
for j in in_arr:
    if (j%7 == 0)and(j%5 != 0):
        print(j, end=' ')
    
