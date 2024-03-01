#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    summation = 0
    for i in range(1, length):
        summation += int(sys.argv[i])
    print(summation)
