import json
import sys


def form_blocks(body):
    for instr in body:
        print(instr)


def mycfg():
    prog = json.load(sys.stdin)
    for func in prog['functions']:
        form_blocks(func['instrs'])


if __name__ == '__main__':
    mycfg()
