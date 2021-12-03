
import sys
import Mparser
from TreePrinter import TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "data/example1.m"
        with open(filename, 'r') as file:
            text = file.read()
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Mparser.parser
    ast = parser.parse(text, lexer=Mparser.scanner.lexer)
    ast.printTree()
