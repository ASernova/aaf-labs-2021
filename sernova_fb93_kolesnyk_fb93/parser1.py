from lexer import *
from table_func import *
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

    def create_table(self, command_length):


        if self.tokens_arr[1].type == 'VAR' and self.tokens_arr[2].type == '(':
            for token in self.tokens_arr:
                if token.type == ')':
                    endindex=self.tokens_arr.index(token)
                    break

            if endindex:
                print('Table ' + self.tokens_arr[1].text + ' was created')
                tablename=self.tokens_arr[1]
                print(endindex)
                # CREATE cats (id INDEXED, name INDEXED, favourite_food); - patern metodichka
                columnsname=[]
                indexedcol=[]
                step=2 # as a default
                index=0

                for i in range(3, endindex, step):
                    #CREATE TABLE Cats(rost , ves INDEXED, cheto, golova INDEXED)
                    if self.tokens_arr[i].type=="COMA":
                        i+=1

                    if self.tokens_arr[i].type=="VAR" and self.tokens_arr[i+1].type=="INDEXED" and (self.tokens_arr[i+2].type=="COMA" or self.tokens_arr[i+2].type==")"):
                        columnsname.append(self.tokens_arr[i].text)
                        indexedcol.append(index)
                    elif self.tokens_arr[i].type=="VAR" and (self.tokens_arr[i+1].type=="COMA" or self.tokens_arr[i+1].type==")"):
                        columnsname.append(self.tokens_arr[i].text)
                    # else:
                    #     self.error()
                    index += 1
                print(columnsname)
                print("Indexed"+str(indexedcol))
                # create_func(columnsname, indexedcol)

                # удалим создание (засунем в массив и выполним)

                table_creation(columnsname, indexedcol) # from file table_func.py
                print("Table created")
                for i in range(0, endindex + 1):
                    self.tokens_arr.pop(0)

        else:
            print("CREATE TABLE TABLENAME (fields INDEXED[optional])")



    def insert(self, comand_length):
        #   INSERT tablename (“2”, “Pushok”, “Fish”)
        if self.tokens_arr[1].type == 'VAR'and self.tokens_arr[2].type == '(' and self.tokens_arr[3].type == 'STR':
            for token in self.tokens_arr:
                if token.type == ')':
                    endindex=self.tokens_arr.index(token)
                    break
            tablename = self.tokens_arr[1].text

            if endindex:
                values=[]
                print(endindex)
                for i in range(3, endindex):
                    if i%2==1:
                        if self.tokens_arr[i].type=="STR":
                            values.append(self.tokens_arr[i].text)
                        else:
                            self.error()
                    else:
                        print(self.tokens_arr[i].text)
                        if self.tokens_arr[i].type == "COMA":
                            continue
                        else:
                            self.error()
            for i in range(len(values)):
                values[i]=values[i].replace("\"", "")
            print(values)
            print("inserted?")
            for i in range(0, endindex + 1):
                self.tokens_arr.pop(0)

                # i = 4
                # for i in range(comand_length-1):
                #     if self.tokens_arr[i].type == 'VALUES':
                #         if self.tokens_arr[i+1].type == '(':
                #             if self.tokens_arr[comand_length-1].type == ')':
                #                 print('new data inserted into "' + self.tokens_arr[1].text + '" into selected columns')
                #                 return True
            # else:
            #     if self.tokens_arr[2].type == 'VALUES':
            #          if self.tokens_arr[3].type == '(':
            #              if self.tokens_arr[comand_length-1].type == ')':
            #                  print('new data inserted into "' + self.tokens_arr[1].text + '"')
            #                  return True
        else:
            self.error()

    def select(self, comand_length):

        if self.tokens_arr[1].type == 'VAR' or self.tokens_arr[1].type == 'ALL':
            if self.tokens_arr[2].type == 'FROM':
                if self.tokens_arr[3].type == 'VAR':
                    if self.tokens_arr[4].type != 'WHERE' and self.tokens_arr[4].type != 'ORDER_BY':
                        print('All ' + self.tokens_arr[1].text + ' was selected from ' + self.tokens_arr[3].text)
                    if self.tokens_arr[4].type == 'WHERE':
                        if self.tokens_arr[6].type == 'EQUAL' or self.tokens_arr[6].type == 'LESS' or self.tokens_arr[6].type == 'MORE' or self.tokens_arr[6].type == 'NOT_EQUAL' or self.tokens_arr[6].type == 'MORE_EQUAL' or self.tokens_arr[6].type == 'LESS_EQUAL':
                        #кастыльный вариант как паттерн, на выходных уберутся жесткие индексы, так как поиск может быть из нескольких колонок/таблиц
                            if self.tokens_arr[8].type != 'ORDER_BY':
                                print('All ' + self.tokens_arr[1].text + 'where' + self.tokens_arr[5].text + self.tokens_arr[5].type.lower() + self.tokens_arr[7].text +' was selected from ' + self.tokens_arr[3].text)
                            if self.tokens_arr[8].type == 'ORDER_BY':
                                if self.tokens_arr[10].type == 'ASC' or self.tokens_arr[10].type == 'DESC':
                                    print('All ' + self.tokens_arr[1].text + 'where' + self.tokens_arr[5].text + self.tokens_arr[5].type.lower() + self.tokens_arr[7].text +' was selected from ' + self.tokens_arr[3].text + ' and sorted')
                    if self.tokens_arr[4].type == 'ORDER_BY':
                        if self.tokens_arr[6].type == 'ASC' or self.tokens_arr[6].type == 'DESC':
                            print('All ' + self.tokens_arr[1].text + ' was selected from ' + self.tokens_arr[3].text + 'and sorted')
        else:
            self.error()

    def start(self):
        comand_length = len(self.tokens_arr)
        if self.tokens_arr[0].type == 'CREATE TABLE':
            self.create_table(comand_length)
        elif self.tokens_arr[0].type == 'INSERT':
            self.insert(comand_length)
        elif self.tokens_arr[0].type == 'SELECT':
            self.select(comand_length)
        elif self.tokens_arr.type=="SEMICOLON":
            return "end"
        elif self.tokens_arr.len==0:
            return "empty"
        #self.tokens_arr[0].type != 'CREATE TABLE' and self.tokens_arr[0].type != 'INSERT INTO' and self.tokens_arr[0].type != 'SELECT'
        else :
            self.error()
