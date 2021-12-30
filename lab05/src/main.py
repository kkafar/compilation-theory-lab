
import sys
import Mparser
import scanner
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker, error_flag
from Interpreter import Interpreter

if __name__ == '__main__':

    try:
        filename = f"data/{sys.argv[1]}.m" if len(sys.argv) > 1 else "data/fibonacci.m"
        with open(filename) as file:
            text = file.read()
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Mparser.parser

    ast = parser.parse(text, lexer=scanner.lexer)

    if not Mparser.error_flag:
        # Below code shows how to use visitor
        typeChecker = TypeChecker()
        typeChecker.visit(ast)   # or alternatively ast.accept(typeChecker)
        # ast.printTree()
        if not error_flag:
            ast.accept(Interpreter())
