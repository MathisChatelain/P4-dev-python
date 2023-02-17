import random

import views.main as main_view
from controllers.crud import (
    create_player,
    create_tournament,
    recreate_player_from_data,
    recreate_tournament_from_data,
    retrieve_player,
    retrieve_tournament,
)
from controllers.inputs import input_number_of_players, input_uuid_or_int
from models.player import Player
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
    if (number_of_players_to_add + len(tournament.players_instances)) % 2 == 1:
        print("Le nombre de joueurs doit être pair, ajout d'un joueur supplémentaire")
        number_of_players_to_add += 1
    while number_of_players_to_add > 0:
        print(f"Joueur n°{index}:")
        player = create_player()
        player.save_in_db()
        tournament.players.append(str(player.uuid))
        tournament.players_instances.append(player)
        number_of_players_to_add -= 1
        index += 1


def play_turn(tournament: Tournament, round):
    players: list[Player] = tournament.players_instances
    if round == 1:
        random.shuffle(players)
    else:
        players = sorted(tournament.players_instances, key=lambda x: x.score)

    for player1, player2 in zip(players[::2], players[1::2]):
        main_view.display_match(player1, player2)
        match_result = play_match(player1, player2)
        player1.score += match_result[0][1]
        player2.score += match_result[1][1]
    # ASKED FIX: save players score after each turn
    for player in players:
        player.save_in_db()
    tournament.save_in_db()


def play_tournament(tournament: Tournament = None):
    players: list[Player] = tournament.players_instances
    if tournament is None:
        print("Aucun tournoi en cours ou chargé, création d'un nouveau tournoi:")
        tournament = create_tournament()
    if len(tournament.players) == 0:
        print("Aucun joueur n'est inscrit au tournoi, veuillez en ajouter:")
        add_players(tournament)
    if tournament.current_round == 0:
        for player in players:
            player.score = 0
            player.save_in_db()

    if tournament.current_round >= tournament.rounds:
        print("Ce tournoi est terminé !")
        tournament_menu(tournament)
    tournament_restart = False
    for current_round in range(1, tournament.rounds + 1):
        if tournament_restart:
            pass
        if current_round <= tournament.current_round:
            print(
                f"Tour {current_round} déjà joué pour ce tournoi, passage au tour suivant"
            )
            continue
        else:
            main_view.display_turn(tournament, current_round)
            play_turn(tournament, current_round)
        tournament_restart = tournament_menu(tournament) == "restart"
    if not tournament_restart:
        main_view.display_tournament_results(tournament)


# ASKED FIX: add tournament menu/reporting
def tournament_menu(tournament: Tournament):
    execute_program = True
    while execute_program:
        choice = input(
            """
            Que souhaitez vous faire aec ce tournoi ?
            Afficher le classement : 1,
            Afficher la liste des joueurs: 2
            Relancer le tournoi à 0: 3,
            Continuer : *autre touche*
            """
        )
        match choice:
            case "1":
                main_view.display_tournament_results(tournament)
            case "2":
                main_view.display_aplhabetical_list_of_tournament_players(tournament)
            case "3":
                tournament.current_round = 0
                for player in tournament.players_instances:
                    player.score = 0
                    player.save_in_db()
                tournament.save_in_db()
                return "restart"
            case _:
                execute_program = False


# ASKED FIX: add player menu/reporting
def player_menu(player: Player):
    execute_program = True
    while execute_program:
        choice = input(
            """
            Que souhaitez vous faire avec ce joueur ?
            Afficher les infos : 1,
            Modifier les infos : 2,
            Continuer : *autre touche*
            """
        )
        match choice:
            case "1":
                main_view.display_player_data(player)
            case "2":
                player = update_player(player)
            case _:
                execute_program = False
    return player


def tournaments_reporting():
    main_view.display_tournament_list()
    tournament_id_or_uuid = input_uuid_or_int()
    tournament_data = retrieve_tournament(tournament_id_or_uuid)
    tournament = recreate_tournament_from_data(tournament_data)
    tournament_menu(tournament)


def players_reporting():
    main_view.display_player_list()
    player_id_or_uuid = input_uuid_or_int()
    player_data = retrieve_player(player_id_or_uuid)
    player = recreate_player_from_data(player_data)
    player_menu(player)


def update_player(player: Player):
    old_uuid = player.uuid
    updated_player = create_player()
    updated_player.uuid = old_uuid
    updated_player.save_in_db()
    return updated_player


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
