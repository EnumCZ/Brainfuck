import sys
from Brainfuck import Brainfuck
from Tokenizer import Tokenizer


def run(source_code):
    tokens = Tokenizer.tokenize(source_code)
    bf = Brainfuck(tokens)
    bf.evaluate()
    #print(bf.cell_list)


filename = sys.argv[1]
source_code = open(filename, 'r').read()

run(source_code)
