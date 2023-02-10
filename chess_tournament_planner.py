from models.tournament import Tournament
from models.player import Player
import views.main as main_view
import controllers.main as main_controller
import controllers.crud as crud_controller

main_view.display_welcome_message()

execute_program = True
while execute_program:
    choice = input(
        """
        Que souhaitez vous faire ?
        Nouveau tournoi : 1,
        Reprendre un tournoi : 2,
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
        case _:
            execute_program = False
