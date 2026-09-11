import json
import sys

TERMINATORS = 'jmp', 'br', 'ret'

def form_blocks(body):
    curr_block = []
    for instr in body:
        if 'op' in instr: 
            curr_block.append(instr)

            if instr['op'] in TERMINATORS: 
                yield curr_block
                curr_block = []

        else: 
            yield curr_block
            curr_block = [instr]
    yield curr_block


def mycfg():
    prog = json.load(sys.stdin)
    for func in prog['functions']:
        for block in form_blocks(func['instrs']):
            print(block)


if __name__ == '__main__':
    mycfg()
