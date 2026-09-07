import json
import sys

def mycfg():
    prog = json.load(sys.stdin)
    print(prog)

if __name__ == '__main__':
    mycfg()