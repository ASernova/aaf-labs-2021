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
    'VAR':TokenPatern('VAR', '[_a-zA-Z0-9]+'),
    'NUMBER': TokenPatern('NUMBER', '[0-9]([0-9.]*)' ),
    'SELECT':TokenPatern('SELECT', 'SELECT'),
    'FROM':TokenPatern('FROM', 'FROM'),
    'INSERT INTO':TokenPatern('INSERT INTO', 'INSERT INTO'),
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
    'SEMICOLON':TokenPatern('SEMICOLON', ';')
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
                self.TokenArr.append(Token(tokenpat.type, result[0], self.pos))
                return True
        raise Exception('Unknown token on position', self.pos)


a = Lexer('SELECT something FROM somewhere WHERE par1 = 15 GROUP_BY par1;')
a.codeanalys()

tokens = a.getTokenArr()
for token in tokens:
    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')