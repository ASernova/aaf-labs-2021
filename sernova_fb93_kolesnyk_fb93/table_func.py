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
    def __init__(self, val_arr, is_null = 0):
        self.values = []
        self.is_null = is_null
        for i in range (0, len(val_arr)):
            self.values.append(val_arr[i])
    

class Table:
    columns = []
    rows = []
    tablename = ''
    
    def __init__(self, name, columns_arr, index_arr):
        self.tablename = name
        self.rows = []
        self.columns.clear()
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
            if self.rows[i].is_null == 0:
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


def select_in_table(fields, table, where_statement, order_statement):
    selected_columns = []
    selected_rows = []
    sel_ind = []
    for i in tables_arr:
        if i.tablename == table.text:
            curr_tab = i
    if fields == 'ALL':
        for i in range(0, len(curr_tab.columns)):
            selected_columns.append(curr_tab.columns[i].name)
            sel_ind = [0]*len(selected_columns)
    if where_statement == 0 and order_statement == 0:
        selected_rows = curr_tab.rows

    sel_tab = Table('selectiom', selected_columns, sel_ind)
    sel_tab.rows = selected_rows
    col_names = []
    for i in range(0, len(sel_tab.columns)):
        col_names.append(sel_tab.columns[i].name)
    print('SELECTION RESULT:')
    sel_tab.show_table()


def del_func(table,cond):
    for i in tables_arr:
        if i.tablename == table.text:
            curr_tab = i
    if cond == "ALL":
        print(str(len(curr_tab.rows))  + ' rows have been deleted from the ' + curr_tab.tablename)
        i = tables_arr.index(curr_tab)
        tables_arr.pop(i)

      #  print(len(tables_arr))
        return
    cond_arr = []
    for i in range(0, len(cond)):
        cond_arr.append(cond[i].text)
     #   print(cond[i].text)
    if len(cond_arr) >1:
        col_name = cond_arr[0]
        condition = cond_arr[1]
        key = cond_arr[2].replace('"', '')
        for col in curr_tab.columns:
            if col.name == col_name:
                column = col

        # index = 0
        indexes = []
        ind_check = 0
        if column.indexed == 1:

            while ind_check == 0:
                index = column.index_tree.searchTree(key).index

                if index != -1:
                    indexes.append(index)
                    column.index_tree.delete_node(key)
                else:
                    ind_check = 1


        else:
            while ind_check == 0:
                if key in column.value_arr:

                    index = column.value_arr.index(key)
                    column.value_arr.pop(index)
                    column.value_arr.insert(index, '0')
                    indexes.append(index)

                else:
                    ind_check = 1

        if condition == '==':
            for index in indexes:
                curr_tab.rows.pop(index)
                curr_tab.rows.insert(index, Row([0] * len(curr_tab.columns), 1))


        if condition == '!=':
            for i in range(0, len(curr_tab.rows)):
                if (i in indexes) == 0:
                    curr_tab.rows.pop(i)
                    curr_tab.rows.insert(index, Row([0] * len(curr_tab.columns), 1))
        print(str(len(indexes))  + ' rows have been deleted from the ' + curr_tab.tablename)




