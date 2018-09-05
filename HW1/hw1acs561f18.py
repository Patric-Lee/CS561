# Author: Li Pengcheng

def input_parsing(filename):
    '''
    Parsing the input file.
    '''
    envs = []
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
        envs = [line.replace('\n', '').split(',') for line in lines]

    return envs

def logic(envs):
    '''
    Args: envs: List of two strings. The first one represents the room, while the second the state (clean or dirty).
    '''
    ans = []
    for env in envs:
        if(env[-1] == "Dirty"):
            ans.append("Suck\n")
        elif(env[0] == "A"):
            ans.append("Right\n")
        else:
            ans.append("Left\n")
    return ans

def output_printing(filename, ans):
    with open(filename, "w") as output_file:
        output_file.writelines(ans)


envs = input_parsing("input.txt")
output_printing("output.txt", logic(envs))