from datetime import datetime
from uuid import UUID


def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un nombre entier")


def input_time_mode(message):
    choices = {"": "bullet", "bullet": "bullet", "blitz": "blitz", "fast": "fast"}
    while True:
        try:
            return choices[input(message)]
        except KeyError:
            print(
                "Choix de mode de jeu invalide:\n Choix possibles : bullet ( par défaut ), blitz, fast"
            )


def input_date(message):
    while True:
        date_str = input(message)
        try:
            return str(datetime.strptime(date_str, "%d-%m-%Y").date())
        except ValueError:
            print("Veuillez entrer une date valide, format: JJ-MM-AAAA")


def input_uuid_or_int(message=None):
    if message is None:
        message = "Veuillez entrer un entier ou un UUID valide :"
    while True:
        value = input(message)
        try:
            return str(UUID(value))
        except ValueError:
            pass
        try:
            return str(int(value))
        except ValueError:
            pass
        print(f"Votre valeur : {value} n'est ni un entier ni un UUID valide")


def input_number_of_players(message):
    nb = 0
    while True or (nb % 2 == 0 and nb >= 2):
        try:
            nb = int(input(message))
            if nb % 2 == 0 and nb >= 2:
                return nb
            else:
                print("Veuillez entrer un nombre entier pair supérieur à 2")
        except ValueError:
            print("Veuillez entrer un nombre entier pair supérieur à 2")
