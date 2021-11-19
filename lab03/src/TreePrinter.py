from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        print('START')
        for child in self.children:
            child.printTree(indent+1)


    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print(self.value)

        for child in self.children:
            child.printTree(indent+1)


    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print(self.value)

        for child in self.children:
            child.printTree(indent+1)


    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass    


        # fill in the body


    # define printTree for other classes
    # ...


