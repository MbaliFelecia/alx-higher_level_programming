#!/usr/bin/python3
if __name__ == "___main__":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[1:]:
            result += int(arg)
    print(result)
