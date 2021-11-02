### all for tables like objects


tables_arr = [] 

class Column:
    def __init__(self, name, indexed):
        self.name = name
        self.indexed = indexed

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
        col_names = []
        for i in range (0, len(self.columns)):
            col_names.append(self.columns[i].name)
        print('Table '+ self.tablename + ' with columns ' + str(col_names))
        self.show_rows()
    
    def insertion(self, row_arr):
        err = 0
        check = 0 
        
        if len(row_arr)!=len(self.columns):
            print('invalind length')
        else: 
           
            row_values = []
           
            for i in range (0, len(self.columns)):
                if self.columns[i].indexed == 0:
                    
                    row_values.append(row_arr[i])
                elif self.columns[i].indexed == 1:
                    check = self.check_repeat(row_arr[i], i)
                    if check == 0:
                        row_values.append(row_arr[i])
                    else:
                        err = 1
                        print('indexed field must be uniaque!')
            
            
            if err !=1:
                self.rows.append(Row(row_values))
