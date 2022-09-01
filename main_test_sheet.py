import sys
import sqlite3
import pathlib



ROOT = ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db2.db")
db_con = sqlite3.connect(DB_FILE)


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
    def rezervari_menu():
        return {
            "perioada": input("Adauga perioada dorita a rezervarii:"),
        } 

user_input = Menu.client_menu()
bike_input = Menu.bike_menu()
rezervare_input = Menu.rezervari_menu()




class DataBase:

    def __init__(self, connection):
        self.conn = sqlite3.connect(connection)


    def create_client_table(self):
        self.conn.cursor()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS clienti (
            id INTEGER PRIMARY KEY,
            nume TEXT NOT NULL,
            prenume TEXT NOT NULL,
            adresa TEXT NOT NULL,
            telefon TEXT NOT NULL,
            cnp TEXT NOT NULL,
            email TEXT NOT NULL)"""
            )
        self.conn.commit()


    def create_rezervation_table(self):
        self.conn.cursor()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS rezervari (
            id INTEGER PRIMARY KEY,
            data_start DATE,
            perioada INTEGER,
            bike_id,
            client_id)""" )
        self.conn.commit()


    def create_moto_table(self):
        self.conn.cursor()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS motociclete(
            id INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            model TEXT NOT NULL,
            an_fabricatie INTEGER NOT NULL,
            tip_cadru_motocicleta TEXT NOT NULL,
            seria_sasiu TEXT NOT NULL,
            numar_inmatriculare TEXT NOT NULL)"""
            )
        self.conn.commit()



    def insert_info_clienti(self, client_data):
        self.conn.cursor()
        self.conn.execute(
            client_data["nume"],
            client_data["prenume"],
            client_data["adresa"],
            client_data["telefon"],
            client_data["cnp"],
            client_data["email"]
            )
        self.conn.commit()

    def insert_info_moto(self, bike_data):
        self.conn.cursor()
        self.conn.execute(
            bike_data["marca"],
            bike_data["model"],
            bike_data["an_fabricatie"],
            bike_data["tip_cadru_motocicleta"],
            bike_data["seria_sasiu"],
            bike_data["nr_inmatriculare"]
            )
        self.conn.commit()

    def insert_info_rezervari(self, rezervari_data):
        self.conn.cursor()
        self.conn.execute(rezervari_data["perioada"])
        self.conn.commit()

    def print_rezervari(self):
        bike = self.conn.cursor()  
        rows = bike.execute()
        row_list = list(rows)
        for i in row_list:
            print(rezervari1)    
        self.conn.commit()


    # def show_bikes(self):
    #     bike = self.conn.cursor()
    #     rows = bike.execute()
    #     row_list = list(rows)  
    #     for i in row_list:
    #         print(bike1)
    #     self.conn.execute()
        
    # def arata_client(self):
    #     bike1 = self.conn.cursor()
    #     rows = bike1.execute()
    #     row_list = list(rows)
        
    #     for i in row_list:
    #         print


class Client:

    def __init__(self, user_data):
        self.__nume = user_data["nume"]
        self.__prenume = user_data["prenume"]
        self.__adresa = user_data["adresa"]
        self.__telefon = user_data["telefon"]
        self.__cnp = user_data["cnp"]
        self.__email = user_data["email"]

class Bike:
    
    def __init__(self, bike_data):
        self.__marca = bike_data["marca"]
        self.__model = bike_data["model"]
        self.__an_fabricatie = bike_data["an_fabricatie"]
        self.__tip_cadru_motocicleta = bike_data["tip_cadru_motocicleta"]
        self.__seria_sasiu = bike_data["seria_sasiu"]
        self.__nr_inmatriculare = bike_data["nr_inmatriculare"]

class Rezervari:

    def __init__(self,rezervari_data):
        self.__perioada = rezervari_data["perioada"]
        
def __init__(self , bike_data):   
    self.__marca = bike_data["marca"]
    
bike_data = Bike.__init__(self, bike_data)


bike1 = Bike(bike_data)
user1 = Client(user_input)
rezervari1 = Rezervari(rezervare_input)

make_table = DataBase(DB_FILE)
make_table.create_client_table()
make_table.create_moto_table()
make_table.create_rezervation_table()

make_table.insert_info_clienti(user_input)
make_table.insert_info_moto(bike_input)
make_table.insert_info_rezervari(rezervare_input)


menu1 = Menu()
menu1.get_main_menu_choice()

make_table.print_rezervari()
# make_table.show.bikes()
# make_table.show.customers()
# make_table.anuleaza.rezervarea()
make_table.create_client_table()
make_table.create_rezervation_table()
make_table.create_moto_table()

user_input = Menu.client_menu()
bike_input = Menu.bike_flow()
rezervare_input = Menu.rezervari_menu()
bike1 = Bike(bike_input)





