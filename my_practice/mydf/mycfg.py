import json
import sys
from collections import OrderedDict

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
            if curr_block: 
                yield curr_block
            curr_block = [instr]

    if curr_block: 
        yield curr_block

def block_map(blocks):
    out = OrderedDict()

    for block in blocks:
        if 'label' in block[0]:
            name = block[0]['label']
            block = block[1:]
        else:
            name = 'b{}'.format(len(out))

        out[name] = block

    return out

def get_cfg(name2block): 
    """Given a name-to-block mapping, produce a mapping from block names to 
    successor block names. 
    """
    out = {}
    for i, (name, block) in enumerate(name2block.items()):
        last = block[-1]

        if last['op'] in ('jmp', 'br'): 
            succ = last['labels']

        elif last['op'] == 'ret':
            succ = []

        else: 
            if i == len(name2block) - 1: 
                succ = []

            else: 
                succ = [list(name2block.keys())[i + 1]]

        out[name] = succ

    return out


def mycfg():
    prog = json.load(sys.stdin)
    for func in prog['functions']:
        name2block = block_map(form_blocks(func['instrs']))
        for name, block in name2block.items(): 
            print(name)
            print(' ', block)
        cfg = get_cfg(name2block)
        print(cfg)


if __name__ == '__main__':
    mycfg()
