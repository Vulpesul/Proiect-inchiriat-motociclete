import sqlite3
import pathlib

ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db2.db")


class Menu:

    @staticmethod
    def bike_menu():
        return {
            "marca": input("Adauga marca:"),
            "model": input("Adauga model:"),
            "an_fabricatie": input("Adauga anul fabricatiei:"),
            "tip_cadru_motocicleta": input("Adauga tipul cadrului:"),
            "seria_sasiu": input("Adauga seria de sasiu:"),
            "numar_inmatriculare": input("Adauga numarul de inmatriculare:")
        }

    @staticmethod
    def client_menu():
        return {
            "nume": input("Adauga numele:"),
            "prenume": input("Adauga prenumele:"),
            "adresa": input("Adauga adresa:"),
            "telefon": input("Adauga numarul de telefon:"),
            "cnp": input("Adauga CNP:"),
            "email": input ("Adauga email:")
        }
    @staticmethod
    def add_rezervari_menu():
        return {
            "perioada": input("Adauga perioada dorita a rezervarii"),
        } 




