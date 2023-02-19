import uuid

from tinydb import TinyDB

db = TinyDB("./db.json")
tournament_table = db.table("tournament_table")


class Tournament:
    def __init__(
        self,
        name,
        location,
        date,
        rounds=4,
        current_round=0,
        description="",
        time_mode="bullet",
        players=[],
    ):
        self.uuid = uuid.uuid4()
        self.name = name
        self.location = location
        self.date = date
        self.current_round = current_round
        self.rounds = rounds
        self.players = players
        self.players_instances = []
        self.description = description
        self.time_mode = time_mode

    def serialized(self):
        return {
            "uuid": str(self.uuid),
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "rounds": self.rounds,
            "current_round": self.current_round,
            "players": self.players,
            "description": self.description,
            "time_mode": self.time_mode,
        }

    def save_in_db(self):
        ids = []
        for tournament in tournament_table.all():
            if tournament["uuid"] == str(self.uuid):
                ids.append(tournament.doc_id)
        tournament_table.remove(doc_ids=ids)
        tournament_table.insert(self.serialized())
