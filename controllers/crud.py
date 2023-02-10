import uuid

from tinydb import Query, TinyDB, where

from controllers.inputs import input_int, input_time_mode
from models.player import Player
from models.tournament import Tournament

db = TinyDB("./db.json")
tournament_table = db.table("tournament_table")
players_table = db.table("player_table")


#################################### CREATE ####################################


def create_tournament():
    name = input("Nom du tournoi : ")
    location = input("Lieu du tournoi : ")
    date = input("Date du tournoi : ")

    time_mode = input_time_mode("Mode de jeu (bullet, blitz, fast): ")

    rounds = input_int("Nombre de tours : ")

    tournament = Tournament(
        name=name, location=location, date=date, time_mode=time_mode, rounds=rounds
    )
    tournament.players = []
    tournament.players_instances = []
    return tournament


def create_player():
    first_name = input("Prénom du joueur : ")
    last_name = input("Nom du joueur : ")
    date_of_birth = input("Date de naissance du joueur : ")
    INE = input("Identifiant nation d'échecs du joueur : ")
    player = Player(
        firstname=first_name, lastname=last_name, birthdate=date_of_birth, INE=INE
    )
    return player


def recreate_tournament_from_data(data):
    try:
        tournament = Tournament(
            name=data["name"],
            location=data["location"],
            date=data["date"],
            rounds=data["rounds"],
            players=data["players"],
            description=data["description"],
            time_mode=data["time_mode"],
        )
        # Reuse the uuid of the tournament
        tournament.uuid = data["uuid"]
        return tournament
    except:
        print(f"Une erreur est survenue durant le chargement du tournoi")


#################################### RETRIEVE ####################################


def check_number_of_tournament():
    if len(tournament_table.all()) == 0:
        print("Aucun tournoi dans la base de données")
        return None
    else:
        return len(tournament_table.all())


def retrieve_tournament(uuid_or_id):
    if check_number_of_tournament() is None:
        return None
    tournament = Query()
    query = tournament_table.search(tournament["uuid"] == str(uuid_or_id))
    if len(query) == 0:
        return tournament_table.all()[int(uuid_or_id) - 1]
    if len(query) == 1:
        return query[0]
    else:
        print("Aucun tournoi trouvé avec cet identifiant")
        return None
