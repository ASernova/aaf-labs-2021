### all for tables like objects

from prettytable import PrettyTable
from BSTree import *

tables_arr = []

class Column:
    def __init__(self, name, indexed):
        self.name = name
        self.indexed = indexed
        if self.indexed == 1:
            self.index_tree = RedBlackTree()
        elif self.indexed == 0:
            self.value_arr = []

class Row:
    
    def __init__(self, val_arr):
        self.values = []
        for i in range (0, len(val_arr)):
            self.values.append(val_arr[i])
        print('row created with: ' + str(self.values))
    

class Table:
    columns = []
    rows = []
    tablename = ''
    
    def __init__(self, name, columns_arr, index_arr):
        self.tablename = name
        self.rows = []
        
        for i in range (0, len(columns_arr)):
            index_check = 0
            if i in index_arr:
                index_check = 1
            self.columns.append(Column(columns_arr[i], index_check))
    def get_name(self):
        return self.tablename
    def check_repeat(self, value, i):
        for j in range (0, len(self.rows)):
            row = self.rows[j]
            if row.values[i] == value:
                return 1
        return 0

    def show_rows(self):
        for i in range(0, len(self.rows)):
            print(str(i+1)+ '. ' + str(self.rows[i].values))

    def show_table(self):
        mytable = PrettyTable()
        col_names = []
        for i in range (0, len(self.columns)):
            col_names.append(self.columns[i].name)
        mytable.field_names = col_names
        for i in range(0, len(self.rows)):
            mytable.add_row(self.rows[i].values)
        print(mytable)
    #    print('Table '+ self.tablename + ' with columns ' + str(col_names))
      #  self.show_rows()
    
    def insertion(self, row_arr):
        index = len(self.rows)
        if len(row_arr)!=len(self.columns):
            raise Exception('invalid length!')
        else: 
           
            row_values = []
           
            for i in range (0, len(self.columns)):
                if self.columns[i].indexed == 0:
                    self.columns[i].value_arr.append(row_arr[i])
                elif self.columns[i].indexed == 1:
                    self.columns[i].index_tree.insert(row_arr[i], index)
                row_values.append(row_arr[i])
            self.rows.append(Row(row_values))


def select_in_table(fields, tablen, where_statement, order_statement):
    print("Select")
    print(fields)
    print(tablen)
    print(where_statement)
    print(order_statement)

def del_func(table,cond):
    cond_arr = []
    for i in range(0, len(cond)):
        cond_arr.append(cond[i].text)
     #   print(cond[i].text)
    for i in tables_arr:
        if i.tablename == table.text:
            curr_tab = i
    col_name = cond_arr[0]
    condition = cond_arr[1]
    key = cond_arr[2].replace('"', '')
    for col in curr_tab.columns:
        if col.name == col_name:
            column = col

    if column.indexed == 1:
        index = column.index_tree.searchTree(key).index
        column.index_tree.delete_node(key)

    else:
        index = column.value_arr.index(key)

    if condition == '==':
        curr_tab.rows.pop(index)


    if condition == '!=':
        for i in range(len(curr_tab.rows)-1, 0, -1):
            if i != index:
                curr_tab.rows.pop(i)
    curr_tab.show_table()




