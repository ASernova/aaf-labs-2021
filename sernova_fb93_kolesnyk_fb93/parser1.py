from table_func import *
import sys
### Parser :



class Parser(object):
    def __init__(self):
        self.tokens_arr = []
        tables_arr = []

    def __init__(self, comand):
        self.tokens_arr = comand
        tables_arr = []

    def parse(self,com):
        self.tokens_arr = com




    def create_table(self, command_length):
       
        if self.tokens_arr[1].type == 'VAR' and self.tokens_arr[2].type == '(':
            
            for token in self.tokens_arr:
                if token.type == ')':
                    endindex=self.tokens_arr.index(token)
                    break

            if endindex:
                tablename=self.tokens_arr[1].text
                # CREATE cats (id INDEXED, name INDEXED, favourite_food); - patern metodichka
                columnsname=[]
                indexedcol=[]
                step=2 # as a default
                index=0
                i=3
                while(i<endindex):
                    if self.tokens_arr[i].type == "COMA":
                        i += 1
                    if self.tokens_arr[i].type == "VAR" and self.tokens_arr[i + 1].type == "INDEXED" and (
                            self.tokens_arr[i + 2].type == "COMA" or self.tokens_arr[i + 2].type == ")"):
                        columnsname.append(self.tokens_arr[i].text)
                        indexedcol.append(index)

                    elif self.tokens_arr[i].type == "VAR" and (
                            self.tokens_arr[i + 1].type == "COMA" or self.tokens_arr[i + 1].type == ")"):
                        columnsname.append(self.tokens_arr[i].text)
                    else:
                        raise Exception("Pattern: CREATE TABLE tablename (field [INDEXED],...)")
                    i+=2
                    index += 1
                print("Fields: "+str(columnsname))
                print("Indexed"+str(indexedcol))
                # удалим создание (засунем в массив и выполним)
                for i in range(0, endindex + 1):
                    self.tokens_arr.pop(0)
                for table in tables_arr:
                    if table.get_name()==tablename:
                        raise Exception('Table with this name already exists:')
                        return False
                table = Table(tablename, columnsname, indexedcol)
                table.show_table()
                tables_arr.append(table)
            else:
                raise Exception('Invalid syntax in CREATE\n u didnt close parentheses')
        else:
            raise Exception('Invalid syntax in CREATE\n syntax: CREATE TABLE tablename (field [INDEXED],...)')

            
            
    def insert(self, comand_length):
        tablename = ''
        #   INSERT tablename (“2”, “Pushok”, “Fish”)
       
        if self.tokens_arr[1].type == 'VAR'and self.tokens_arr[2].type == '(' and self.tokens_arr[3].type == 'STR':
            for token in self.tokens_arr:
                if token.type == ')':
                    endindex=self.tokens_arr.index(token)
                    break
            tablename = self.tokens_arr[1].text
            for j in range(0, len(tables_arr)):
                if tables_arr[j].tablename == tablename :
                    curr_table = tables_arr[j]
     #               print(curr_table.tablename + ' was found')
                    break
                else:
                    raise Exception('No table with name ' + tablename)
            if endindex:
                values=[]
                for i in range(3, endindex):
                    if i%2==1:
                        if self.tokens_arr[i].type=="STR":
                            values.append(self.tokens_arr[i].text)
                        else:
                            raise Exception('Invalid syntax in INSERT\n syntax: INSERT tablename (“str”...)')
                    else:
                        if self.tokens_arr[i].type == "COMA":
                            continue
                        else:
                            raise Exception('Invalid syntax in INSERT\n syntax: INSERT tablename (“str”...)')
                for i in range(len(values)):
                    values[i]=values[i].replace("\"", "")
                curr_table.insertion(values)
                curr_table.show_table()
                for i in range(0, endindex + 1):
                    self.tokens_arr.pop(0)
            else:
                raise Exception('Invalid syntax in INSERT\n u didnt close parentheses')
        else:
            raise Exception('Invalid syntax in INSERT\n syntax: INSERT tablename (“str”...)')

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
        elif self.tokens_arr[0].type == "EXIT":
            print("exit")
            sys.exit()
        elif self.tokens_arr[0].type=="SEMICOLON":
            return "end"
        elif len(self.tokens_arr) ==0:
            return "empty"
        else :
            raise Exception("Unknown command "+str(self.tokens_arr[0].text)+ " "+ str(self.tokens_arr[1].text) +" use commands (only uppercase for commands)\'CREATE TABLE\' , \'INSERT\', \'SELECT\', \'EXIT\' ")