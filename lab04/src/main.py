
import sys
import Mparser
import scanner
from TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "data/test1.m"
        with open(filename) as file:
            text = file.read()
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Mparser.parser

    ast = parser.parse(text, lexer=scanner.lexer)

    # Below code shows how to use visitor
    typeChecker = TypeChecker()   
    typeChecker.visit(ast)   # or alternatively ast.accept(typeChecker)
    