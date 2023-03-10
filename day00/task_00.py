import sys
from sys import stdin

if __name__ == '__main__':
    counter = 0
    for line in stdin:
        if counter < int(sys.argv[1]):
            if len(line) == 33 and line.find("00000") == 0:
                if line[5] != '0':
                    print(line)
        counter+=1
