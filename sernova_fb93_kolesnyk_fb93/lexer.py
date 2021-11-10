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

tokensdictionary = {
    'CREATE TABLE':TokenPatern('CREATE TABLE', 'CREATE TABLE'),
    'INDEXED':TokenPatern('INDEXED', 'INDEXED'),
    'COMA':TokenPatern('COMA', ','),
    'SPACE':TokenPatern('SPACE', '[ \\n\\r\\t]'),
    '(':TokenPatern('(', '\\('),
    ')':TokenPatern(')', '\\)'),
    '[':TokenPatern('[', '\\['),
    ']':TokenPatern(']', '\\]'),
    # 'NUM': TokenPatern('NUM', '[0-9]([0-9.]*)' ),
    'SELECT':TokenPatern('SELECT', 'SELECT'),
    'FROM':TokenPatern('FROM', 'FROM'),
    'INSERT':TokenPatern('INSERT', 'INSERT'),
    'VALUES':TokenPatern('VALUES', 'VALUES'),
    'WHERE':TokenPatern('WHERE', 'WHERE'),
    'GROUP_BY':TokenPatern('GROUP_BY', 'GROUP_BY'),
    'ASC':TokenPatern('ASC', 'ASC'),
    'DESC':TokenPatern('DESC', 'DESC'),
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
    'VAR':TokenPatern('VAR', '[_a-zA-Z0-9]+'),
    'STR':TokenPatern('STR', '\"+[a-zA-Z0-9]+\"'),
    'EXIT':TokenPatern('EXIT', "EXIT")
}


class Lexer:
    index = 0
    code = ''
    TokenArr = []

    def __init__(self):
        self.code=""

    def __init__(self, code):
        self.code = code

    def getTokenArr(self):
        return self.TokenArr

    def NewCode(self,code):
        self.code = code


    def CodeToTokens(self):
        while self.nexttok():
            continue
        comand = []
        for token in self.TokenArr:
            if token.type != 'SPACE':
                comand.append(token)
        return comand

    def nexttok(self):
        #End of the code
        if self.index == (len(self.code)):
            return False
        for tokenpatern in tokensdictionary.values():
            result = re.search('^' + tokenpatern.regexp, self.code[self.index:])
            if result:
                self.index = self.index + len(result[0])
              #  if token.type != 'SPACE':
                self.TokenArr.append(Token(tokenpatern.type, result[0], self.index))
                return True
        raise Exception('Unknown token on position ' + str(self.index))

