import re

class TokenPatern:
    def __init__(self, type, regexp):
        self.type = type
        self.regexp = regexp

class Token:
    def __init__(self, type, text, pos):
        self.type = type
        self.text = text
        self.pos = pos

TokenPaterns = {
    'CREATE TABLE':TokenPatern('CREATE TABLE', 'CREATE TABLE'),
    'INDEXED':TokenPatern('INDEXED', 'INDEXED'),
    'COMA':TokenPatern('COMA', ','),
    'SPACE':TokenPatern('SPACE', '[ \\n\\r\\t]'),
    '(':TokenPatern('(', '\\('),
    ')':TokenPatern(')', '\\)'),
    '[':TokenPatern('[', '\\['),
    ']':TokenPatern(']', '\\]'),
    'NUMBER': TokenPatern('NUMBER', '[0-9]([0-9.]*)' ),
    'SELECT':TokenPatern('SELECT', 'SELECT'),
    'FROM':TokenPatern('FROM', 'FROM'),
    'INSERT INTO':TokenPatern('INSERT INTO', 'INSERT INTO'),
    'VALUES':TokenPatern('VALUES', 'VALUES'),
    'WHERE':TokenPatern('WHERE', 'WHERE'),
    'GROUP_BY':TokenPatern('GROUP_BY', 'GROUP_BY'),
    'DELETE':TokenPatern('DELETE', 'DELETE'),
    'EQUAL': TokenPatern('EQUAL', '= '),
    'NOT_EQUAL':TokenPatern('NOT_EQUAL', '!='),
    'MORE_EQUAL':TokenPatern('MORE_EQUAL', '>='),
    'LESS_EQUAL': TokenPatern('LESS_EQUAL', '<='),
    'LESS':TokenPatern('LESS', '<'),
    'MORE':TokenPatern('MORE', '>'),
    'ALL':TokenPatern('ALL', '\\*'),
    'COUNT':TokenPatern('COUNT', 'COUNT'),
    'COUNT_DISTINCT':TokenPatern('COUNT_DISTINCT', 'COUNT_DISTINCT'),
    'MAX':TokenPatern('MAX', 'MAX'),
    'AVG':TokenPatern('AVG', 'AVG'),
    'SEMICOLON':TokenPatern('SEMICOLON', ';'),
    'VAR':TokenPatern('VAR', '[_a-zA-Z0-9]+')
  

}


class Lexer:
    pos = 0
    code = ''
    TokenArr = []

    def __init__(self, code):
        self.code = code

    def getTokenArr(self):
        return self.TokenArr

    def codeanalys(self):
        try:
            while self.nexttok():
                continue
        except Exception as error:
            text, pos = error.args
            print(text + ' ' + str(pos) + ": " + self.code[self.pos:self.pos + 10])

    def nexttok(self):
        if self.pos == (len(self.code)):
            return False
        for tokenpat in TokenPaterns.values():
            result = re.search('^' + tokenpat.regexp, self.code[self.pos:])
            if result:
                self.pos = self.pos + len(result[0])
              #  if token.type != 'SPACE':
                self.TokenArr.append(Token(tokenpat.type, result[0], self.pos))
                return True
        raise Exception('Unknown token on position', self.pos)

### Parser:

class Parser(object):
    def __init__(self, comand):
        self.tokens_arr = comand

    def error(self):
        raise Exception('Invalid syntax')

#    def write_token(self, token_type):
 #       if self.current_token.type == token_type:
  #          self.current_token = self.lexer.nexttok()
   #     else:
    #        self.error()
    
    def create_table(self, comand_length):
        if self.tokens_arr[1].type == 'VAR' and self.tokens_arr[2].type == '(' and self.tokens_arr[comand_length-1].type == ')':
            print('Table ' + self.tokens_arr[1].text + ' was created')
        else:
            self.error()

    def insert(self, comand_length):
        if self.tokens_arr[1].type == 'VAR':
            if self.tokens_arr[2].type == '(' :
                if self.tokens_arr[3].type == 'VAR':
                    i = 4
                    for i in range(comand_length-1):
                        if self.tokens_arr[i].type == 'VALUES':
                            if self.tokens_arr[i+1].type == '(':
                                if self.tokens_arr[comand_length-1].type == ')':
                                    print('new data inserted into "' + self.tokens_arr[1].text + '" into selected columns')
                                    return True
            else:
                if self.tokens_arr[2].type == 'VALUES':
                     if self.tokens_arr[3].type == '(':
                         if self.tokens_arr[comand_length-1].type == ')':
                             print('new data inserted into "' + self.tokens_arr[1].text + '"')
                             return True
            self.error()

    def select(self, comand_length):
     
        if self.tokens_arr[1].type == 'VAR' or self.tokens_arr[1].type == 'ALL':
            if self.tokens_arr[2].type == 'FROM':
                if self.tokens_arr[3].type == 'VAR':
                    
                    print('Start selection but without real structure we cant predict if it would be successfull')
        else:
            self.error()


    def start(self):
        comand_length = len(self.tokens_arr)
        if self.tokens_arr[0].type == 'CREATE TABLE':
            self.create_table(comand_length)
        if self.tokens_arr[0].type == 'INSERT INTO':
            self.insert(comand_length)
        if self.tokens_arr[0].type == 'SELECT':
            self.select(comand_length)

        if self.tokens_arr[0].type != 'CREATE TABLE' and self.tokens_arr[0].type != 'INSERT INTO' and self.tokens_arr[0].type != 'SELECT':
            self.error()

b = Lexer('CREATE TABLE Cats(sdjdf, lksd)')
c = Lexer('INSERT INTO Cats (jndsn) VALUES (skjd, skd, m)')
d = Lexer('SELECT * FROM sdjfljsdf')
e = Lexer ('unexpected CREATE TABLE kfksf (sdjf)')
a = Lexer('SELECT something FROM somewhere WHERE par1 = 15 GROUP_BY par1;')

b.codeanalys()
comand = []

tokens = b.getTokenArr()
for token in tokens:
    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')

for token in tokens:
    if token.type != 'SPACE' :
        comand.append(token)

#for token in comand:
#    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')


parser = Parser(comand)
parser.start();