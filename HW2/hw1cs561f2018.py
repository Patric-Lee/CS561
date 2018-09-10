import time

start = time.time()
def input_parsing(filename):
    with open(filename, 'r') as input_file:
        n = input_file.readline()
        p = input_file.readline()
        s = input_file.readline()
        lines = input_file.readlines()

    return n, p, s, lines

solutions = []
def put_officer(n, p, officers):
    if(p == 0):
        #solutions.append(officers[:])
        #print len(solutions)
        #print officers[:]
        return;
    s = officers[-1][0] + 1 if len(officers) > 0 else 0
    for i in range(s, n):
        flag = False
        for officer in officers:
            if(officer[0] == i):
                flag = True
                break;
        if(flag):
            continue;
        for j in range(n):
            flag = False
            for officer in officers:
                if(officer[1] == j):
                    flag = True
                    break;
                if(officer[0] - i == officer[1] - j or officer [0] - i + officer[1] - j == 0):
                    flag = True
                    break;
            if(flag):
                continue;
            officers.append((i, j))
            put_officer(n, p - 1, officers)
            officers.pop()

n = 8
p = 8
put_officer(n, p, [])
#print len(solutions)
end = time.time()
print end - start
