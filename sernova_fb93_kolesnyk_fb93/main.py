from parser1 import *
from lexer import *


b = Lexer('CREATE TABLE Cats (rost INDEXED, ves, color INDEXED, golova) INSERT Cats ("2", "Pushok", "Fish", "Has") INSERT Cats ("4", "Vasiliy", "Black", "No")')

b.CodeToTokens()
comand = []
tokens = b.getTokenArr()
#for token in tokens:
#    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')
for token in tokens:
    if token.type != 'SPACE':
        comand.append(token)
#for token in comand:
#    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')


parser = Parser(comand)
while len(parser.tokens_arr)!=0:
    parser.start();

