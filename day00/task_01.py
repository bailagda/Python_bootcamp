import sys

if __name__ == '__main__':
    code = sys.argv[1].split(' ')
    passw = ""
    for word in code:
        passw+=word[0]
    print(passw)
