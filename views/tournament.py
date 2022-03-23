from views.setting import Setting
from controller.timesetting import get_timesetting
from controller.database import load_db


class CreateTournament(Setting):

    def display_menu(self):

        date = get_timesetting()
        print("-"*15 + "Création d'un nouveau tournoi : " + date + "-"*15)

        name = input("Nom du tournoi:\n")

        location = self.get_user_entry(
            msg_display="Lieu:\n",
            msg_error="Lieu invalide",
            value_type="string"
        )

        user_selection_time_control = self.get_user_entry(
            msg_display="Contrôle de temps:\n1 - Bullet\n2 - Blitz\n3 - Coup Rapide\n",
            msg_error="Selection invalide (entrer 1, 2 ou 3.)",
            value_type="selection",
            assertions=[ "1", "2", "3"]
        )
        if user_selection_time_control == "1":
            time_control = "Bullet"
        elif user_selection_time_control == "2":
            time_control = "Blitz"
        else:
            time_control = "Coup Rapide"

        nb_players = self.get_user_entry(
            msg_display="Nombre de joueurs:\n",
            msg_error="Entrée invalide (Entrer un chiffre supérieur ou égal à 2.)",
            value_type="num_superior",
            default_value=2
        )

        nb_rounds = self.get_user_entry(
            msg_display="Nombre de tours (4 par défaut):\n",
            msg_error="Entrée invalide (4 par défaut).",
            value_type="num_superior",
            default_value=4
        )
        description = input("Description du tournoi:\n")

        return {
            "name": name,
            "location": location,
            "date": date,
            "time_control": time_control,
            "nb_players": nb_players,
            "nb_rounds": nb_rounds,
            "description": description
        }


class LoadTournament(Setting):

    def display_menu(self):

        all_tournaments = load_db("tournaments")
        if all_tournaments:

            builded_selection = self.build_selection(iterable=all_tournaments,
                                                     display_msg="Choisir un tournoi:\n",
                                                     assertions=[])

            user_input = int(self.get_user_entry(
                msg_display=builded_selection['msg'] + "\n> ",
                msg_error="Veuillez entrer un nombre entier.",
                value_type="selection",
                assertions=builded_selection['assertions']
            ))
            serialized_loaded_tournament = all_tournaments[user_input-1]

            return serialized_loaded_tournament

        else:
            return False