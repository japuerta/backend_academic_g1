from models.candidate import Candidate


class CandidateController:

    def __init__(self):
        print("Candidate Controller ready")

    # Equivalent to 'all'
    def index(self) -> list:
        print("return all candidates")
        data = {
            "id_": "abc123",
            "personal_id": "123456",
            "names": "alvaro",
            "last name": "perez",
            "political party": "liberal"
        }
        candidate = Candidate(data)
        return [candidate.__dict__]

    # Equivalent to 'one by id'
    def show(self, id_: str) -> dict:
        print("return one candidate")
        data = {
            "id_": id_,
            "personal_id": "123456",
            "names": "alvaro",
            "last name": "perez",
            "political party": "liberal"
        }
        candidate = Candidate(data)
        return candidate.__dict__

    # Equivalent to 'insert'
    def create(self, candidate_: dict) ->dict:
        print("insert a candidate")
        candidate = Candidate(candidate_)
        return candidate.__dict__

    def update(self, id_: str, candidate_: dict)->dict:
        print("update an candidate")
        data = candidate_
        data['_id'] = id_
        candidate = Candidate(data)
        return candidate.__dict__

    def delete(self, id_:str)->dict:
        print("delete a candidate" + id_)
        return {"delete count": 1}