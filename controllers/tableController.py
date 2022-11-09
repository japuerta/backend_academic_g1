from models.table import Table


class TableController:

    def __init__(self):
        print("Table Controller ready")

    # Equivalent to 'all'
    def index(self):
         print("return all tables")

    # Equivalent to 'one by id'
    def show(self, id_):
        print("return one table")

    # Equivalent to 'insert'
    def create(self, table_):
        print("insert a table")

    def update(self, id_, table_):
        print("update an table")

    def delete(self, id_):
        print("delete a table")