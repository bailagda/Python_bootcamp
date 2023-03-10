import sys
from sys import stdin

def parse_file(file):
    row = 0
    for line in file:
        if len(line) != 6 or row > 2:

            return 1
        row+=1
    return 0

if __name__ == '__main__':
    file = open(sys.argv[1])
    row = 0
    if parse_file(file) != 0:
        print("Error!")
    else:
        for line in open(sys.argv[1]):
            if row == 0:
                if line[0] != '*' or line[4] != '*' \
                        or line[1] == '*' or line[2] == '*' or line[3] == '*':
                    print(False)
                    break
            elif row == 1:
                if line[0] != '*' or line[1] != '*' \
                        or line[3] != '*' or line[4] != '*' or line[2] == '*':
                    print(False)
                    break
            elif row == 2:
                if line[0] == '*' or line[2] == '*' \
                        or line[4] == '*' or line[1] != '*' or line[3] != '*':
                    print(True)
                    break
            row += 1
        # return 0;
    # for line in file:
        # if len(line) != 4 or rows > 2:
        #     print("Error!")
        #     break
        # else:
        #     if rows == 0 :
        #
        #
    file.close()
