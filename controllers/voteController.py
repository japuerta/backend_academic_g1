from models.vote import Vote


class VoteController:

    def __init__(self):
        print("Vote Controller ready")

    # Equivalent to 'all'
    def index(self):
        print ("return all votes")

    # Equivalent to 'one by id'
    def show(self, id_):
        print ("return one vote")

    # Equivalent to 'insert'
    def create(self, vote_):
        print ("insert a vote")

    def update(self, id_, vote_):
        print("update an vote")

    def delete(self, id_):
        print("delete a vote")