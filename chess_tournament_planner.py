import controllers.crud as crud_controller
import controllers.main as main_controller
import views.main as main_view

main_view.display_welcome_message()

execute_program = True
while execute_program:
    choice = input(
        """
        Que souhaitez vous faire ?
        Nouveau tournoi : 1,
        Reprendre un tournoi : 2,
        Afficher les tournois : 3,
        Afficher les joueurs : 4,
        Gérer les tournois: 5,
        Gérer les joueurs: 6,
        Arret du programme : *autre touche*
        """
    )
    if choice:
        if choice == "1":
            main_controller.play_tournament()
        if choice == "2":
            if crud_controller.check_number_of_tournament() is None:
                pass
            else:
                main_controller.load_tournament()
        if choice == "3":
            main_view.display_tournament_list()
        if choice == "4":
            main_view.display_player_list()
        if choice == "5":
            main_controller.tournaments_reporting()
        if choice == "6":
            main_controller.players_reporting()
        else:
            execute_program = False
