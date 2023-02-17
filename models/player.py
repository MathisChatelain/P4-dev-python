import uuid

from tinydb import TinyDB

db = TinyDB("./db.json")
player_table = db.table("player_table")


class Player:
    def __init__(self, firstname, lastname, birthdate, INE):
        self.uuid = uuid.uuid4()
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.name = f"{firstname} {lastname}"
        self.INE = INE
        self.score = 0

    def serialized(self):
        # we dont want to serialize the score
        return {
            "uuid": str(self.uuid),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthdate": self.birthdate,
            "INE": self.INE,
        }

    def save_in_db(self):
        ids = []
        for player in player_table.all():
            if player["uuid"] == str(self.uuid):
                ids.append(player.doc_id)
        player_table.remove(doc_ids=ids)
        player_table.insert(self.serialized())
