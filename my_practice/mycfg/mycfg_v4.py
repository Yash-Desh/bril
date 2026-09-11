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


def block_map(blocks):
    out = {}

    for block in blocks:
        if 'label' in block[0]:
            name = block[0]['label']
            block = block[1:]
        else:
            name = 'b{}'.format(len(out))

        out[name] = block

    return out

def mycfg():
    prog = json.load(sys.stdin)
    for func in prog['functions']:
        name2block = block_map(form_blocks(func['instrs']))
        print(name2block)


if __name__ == '__main__':
    mycfg()
