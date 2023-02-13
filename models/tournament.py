import uuid

from tinydb import Query, TinyDB

db = TinyDB("./db.json")
tournament_table = db.table("tournament_table")


class Tournament:
    def __init__(
        self,
        name,
        location,
        date,
        rounds=4,
        description="",
        time_mode="bullet",
        players=[],
    ):
        self.uuid = uuid.uuid4()
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.players = players
        self.players_instances = []
        self.description = description
        self.time_mode = time_mode
        self.save_in_db()

    def serialized(self):
        return {
            "uuid": str(self.uuid),
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "rounds": self.rounds,
            "players": self.players,
            "description": self.description,
            "time_mode": self.time_mode,
        }

    def save_in_db(self):
        if db.search(Query().uuid == str(self.uuid)):
            print("test")
            tournament_table.update(self.serialized(), Query().uuid == str(self.uuid))
        else:
            tournament_table.insert(self.serialized())
