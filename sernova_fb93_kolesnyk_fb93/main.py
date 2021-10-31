from parser1 import *
from lexer import *


b = Lexer('INSERT tablename ("2", "Pushok", "Fish")')
b.CodeToTokens()
comand = []
tokens = b.getTokenArr()
for token in tokens:
    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')
for token in tokens:
    if token.type != 'SPACE':
        comand.append(token)
#for token in comand:
#    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')


parser = Parser(comand)
while len(parser.tokens_arr)!=0:
    parser.start();
