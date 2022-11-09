from models.politicalParty import PoliticalParty


class PoliticalPartyController:

    def __init__(self):
        print("Political Party Controller ready")

    # Equivalent to 'all'
    def index(self):
         print("return all Political Parties")

    # Equivalent to 'one by id'
    def show(self, id_):
        print("return one Political Party")

    # Equivalent to 'insert'
    def create(self, politicalParty_):
        print("insert a Political Party")

    def update(self, id_, politicalParty_):
        print("update an Political Party")

    def delete(self, id_):
        print("delete a Political Party")