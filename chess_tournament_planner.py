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
        Arret du programme : *autre touche*
        """
    )
    match choice:
        case "1":
            main_controller.play_tournament()
        case "2":
            if crud_controller.check_number_of_tournament() is None:
                pass
            else:
                main_controller.load_tournament()
        case "3":
            main_view.display_tournament_list()
        case "4":
            main_view.display_player_list()
        case _:
            execute_program = False
