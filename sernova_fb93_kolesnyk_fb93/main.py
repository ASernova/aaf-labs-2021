from parser1 import *
from lexer import *



lex = Lexer()
parser = Parser()
while(True):
    b=input("Enter command: ")
    lex.NewCode(b)
    commands = lex.CodeToTokens()
    parser.parse(commands)
    parser.start()

    # while len(parser.tokens_arr)!=0:
    #     for token in parser.tokens_arr:
    #         if token.type==";" or token.type=="EXIT":
    #             indx=parser.tokens_arr.index(token)
    #             while parser.tokens_arr[indx+1]:
    #                 parser.tokens_arr.pop[indx+1]

