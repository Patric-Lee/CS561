import time
ans = 0
def put_officer(n, row, ld, rd):
    global ans
    calFlag = True
    stack = []
    while(1):
        if(row != n):
            if(calFlag):
                pos = n & (~(row | ld | rd))
            
            while(pos != 0):
                
                p = pos & (~pos + 1)
                pos = pos - p
                #put_officer(n, row | p, (ld | p ) << 1, (rd | p) >> 1)
                stack.append((row, ld, rd, pos))
                row |= p
                ld = (ld | p) << 1
                rd = (rd | p) >> 1
                flag = True
                calFlag = True
                break
        else:
            ans += 1
            flag = False
            
        if(flag):
            flag = False
            continue
        if(len(stack) == 0):
            break
        row, ld, rd, pos = stack.pop()
        calFlag = False
        

start = time.time()
put_officer((1 << 14) - 1, 0, 0, 0)
end = time.time()
print ans
print end - start