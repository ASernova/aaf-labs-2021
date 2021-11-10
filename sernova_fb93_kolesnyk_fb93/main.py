from parser1 import *
from lexer import *



lex = Lexer('CREATE TABLE Cats (rost INDEXED, ves, color INDEXED, golova) INSERT Cats ("2", "Pushok", "Fish", "Has") INSERT Cats ("4", "Vasiliy", "Black", "No")')
commands=lex.CodeToTokens()
parser = Parser(commands)
# while(True):
# b=input("Enter command: ")
# lex.NewCode(b)
while len(parser.tokens_arr)!=0:
    for token in parser.tokens_arr:
        if token.type==";" or token.type=="EXIT":
            indx=parser.tokens_arr.index(token)
            while parser.tokens_arr[indx+1]:
                parser.tokens_arr.pop[indx+1]
    parser.start()

