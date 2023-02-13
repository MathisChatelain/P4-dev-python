import random

import views.main as main_view
from controllers.crud import (
    create_player,
    create_tournament,
    recreate_tournament_from_data,
    retrieve_tournament,
)
from controllers.inputs import input_number_of_players, input_uuid_or_int
from models.tournament import Tournament


def update_time_mode(tournament: Tournament, time_mode):
    choices = ["bullet", "blitz", "fast"]
    if time_mode in choices:
        tournament.time_mode = time_mode
        print(f"Mode de jeu mis à jour avec succés : {time_mode}")
        return 0
    else:
        print(
            f"""
            Choix de mode de jeu invalide:\n Choix possibles :
            {str(choices)[1:-1]}, votre précedente saisie ${time_mode}
            """
        )
        return 1


def add_players(tournament: Tournament):
    index = 1
    number_of_players_to_add = input_number_of_players(
        "Combien de joueurs voulez-vous ajouter ?"
    )
    while number_of_players_to_add > 0:
        print(f"Joueur n°{index}:")
        player = create_player()
        player.save_in_db()
        tournament.players.append(str(player.uuid))
        tournament.players_instances.append(player)
        number_of_players_to_add -= 1
        index += 1


def play_turn(tournament: Tournament, round):
    players = tournament.players_instances
    if round == 1:
        random.shuffle(players)
    else:
        players = sorted(tournament.players_instances, key=lambda x: x.score)

    for player1, player2 in zip(players[::2], players[1::2]):
        main_view.display_match(player1, player2)
        match_result = play_match(player1, player2)
        player1.score += match_result[0][1]
        player2.score += match_result[1][1]
        tournament.save_in_db()


def play_tournament(tournament: Tournament = None):
    if tournament is None:
        print("Aucun tournoi en cours ou chargé, création d'un nouveau tournoi:")
        tournament = create_tournament()
    if len(tournament.players) == 0:
        print("Aucun joueur n'est inscrit au tournoi, veuillez en ajouter:")
        add_players(tournament)
    for round in range(1, tournament.rounds + 1):
        main_view.display_turn(tournament, round)
        play_turn(tournament, round)
    main_view.display_tournament_results(tournament)


def load_tournament():
    main_view.display_tournament_list()
    tournament_id_or_uuid = input_uuid_or_int()
    tournament_data = retrieve_tournament(tournament_id_or_uuid)
    tournament = recreate_tournament_from_data(tournament_data)
    play_tournament(tournament)


def play_match(player_one, player_two):
    results = [0, 0]
    results_inputted = False

    while results_inputted is False:
        results_choice = input(
            f"""
                Veuillez entrer les résultats:
                victoire de {player_one.name} -> 0
                victoire de {player_two.name} -> 1
                match nul -> 2\n
            """
        )
        results_inputted = True
        match results_choice:
            case "0":
                results = [1, 0]
            case "1":
                results = [0, 1]
            case "2":
                results = [0.5, 0.5]
            case _:
                print(
                    f"""
                    Veuillez entrer un nombre entre parmi les choix proposés !
                    Votre entrée : {results_choice} n'est pas valide.
                    """
                )
                results_inputted = False

    print(
        f"Résultats du match : {player_one.name} {results[0]} - {results[1]} {player_two.name}"
    )
    return ([player_one, results[0]], [player_two, results[1]])
