from tinydb import TinyDB

db = TinyDB("./db.json")
tournament_table = db.table("tournament_table")
players_table = db.table("player_table")


def check_number_of_tournament():
    if len(tournament_table.all()) == 0:
        print("Aucun tournoi dans la base de données")
        return None
    else:
        return len(tournament_table.all())


def check_number_of_player():
    if len(players_table.all()) == 0:
        print("Aucun joueur dans la base de données")
        return None
    else:
        return len(players_table.all())


def display_welcome_message():
    print(
        """
        Bienvenue sur le programme de gestion de tournoi d'échecs !
        """
    )


def display_match(player_one, player_two):
    print(
        f"""
        Match entre {player_one.name} et {player_two.name}
        """
    )


def display_tournament_list():
    if check_number_of_tournament() is None:
        return None
    index = 1
    print(
        "################################### Liste des tournois #############################################"
    )
    for tournament in tournament_table:
        print(
            f"""
        Numéro: {index},
        UUID: { tournament["uuid"]  or "non renseigné" },
        Nom: {tournament["name"] or "non renseigné" },
        Date: { tournament["date"]  or "non renseigné" },
        """
        )
        index += 1
    print(
        "------------------------------------ Fin de la liste ----------------------------------------------"
    )


def display_player_list():
    if check_number_of_player() is None:
        return None
    index = 1
    print(
        "################################### Liste des joueurs #############################################"
    )
    for player in players_table:
        print(
            f"""
        Numéro: {index},
        UUID: { player["uuid"]  or "non renseigné" },
        Nom: {(player["firstname"] + " " + player["lastname"]) or "non renseigné" },
        Date de naissance: { player["birthdate"]  or "non renseigné" },
        INE: { player["INE"]  or "non renseigné" },
        """
        )
        index += 1
    print(
        "------------------------------------ Fin de la liste ----------------------------------------------"
    )


def display_turn(tournament, round):
    print(
        f"""
    Tour {round}/{tournament.rounds} du tournoi {tournament.name}, de {tournament.location}, le {tournament.date}
    Tableau des scores:
    """
    )
    display_tournament_results(tournament)


def display_tournament_results(tournament):
    results = ""
    for player in sorted(
        tournament.players_instances, key=lambda x: x.score, reverse=True
    ):
        results += f"{player.name} : {player.score} points\n    "
    print(
        f"""
    {results}
    """
    )


def display_player_data(player):
    print(
        f"""
    Nom : {player.lastname}
    Prénom : {player.firstname}
    Date de naissance : {player.birthdate}
    INE : {player.INE}
    """
    )


def display_aplhabetical_list_of_tournament_players(tournament):
    """
    Display the list of players in alphabetical order
    """
    print(
        f"""
    Liste alphabétique des joueurs du tournoi {tournament.name} :
    """
    )
    for player in sorted(tournament.players_instances, key=lambda x: x.lastname):
        print(
            f"""
        {player.firstname, player.lastname}
        """
        )


def display_tournament_name_and_date(tournament):
    """
    Display the name and date of the tournament
    """
    print(
        f"""
    Tournoi {tournament.name} du {tournament.date}
    """
    )
