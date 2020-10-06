

import mysql.connector as mysql # virtualioje aplinkoje instaliuoti paketa -> pip install mysql.connector
import csv
from input_db import host,user,password,my_database_name

# ------- LISTAS : LENTELIU PAVADINIMAI -------
my_database_table_name = ['IMDBdata', 'Cinema_repertoire','Reservation']

# ------- LENTELIU PAVADINIMUS PAVERCIA I STRINGA. -------
table_names = ",".join(my_database_table_name)

# ------- JUNGIAMES PRIE DUOMENU BAZES -------
connection = mysql.connect(host=f'{host}', # IMPORT IS input_db.py  -> Padaryta input'o uzklausa
                           user=f'{user}', # IMPORT IS input_db.py  -> Padaryta input'o uzklausa
                           password=f'{password}') # IMPORT IS input_db.py  -> Padaryta input'o uzklausa

# ------- PRISIJUNGIA PRIE DUOMENU BAZES -------
cursor = connection.cursor()

# ------- IVYKDO DUOMENU BAZES UZDUOTIS -------
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {my_database_name};") # sukuria duomenu baze pavadinima , kuri priskiria input_db.py

# ------- JUNGIASI PRIE DUOMENU BAZES SU SIUO PRISKIRTU PAVADINIMU -------
connection.connect(database=my_database_name)

# ------- IVYKDO DUOMENU BAZES UZDUOTIS , TAI PANAIKINA LENTELES IS MUSU LISTO , JEI TOKIOS JAU YRA.
cursor.execute(f"DROP TABLE IF EXISTS {table_names};")

# ------- SUKURIA DUOMENU BAZES LENTELES -------
create_table_one = f"""
        CREATE TABLE {my_database_table_name[0]}  # <-- paimtas is musu lenteliu listo
        (
        Movie_Title varchar(200) NOT NULL,
        Yr_Released int NOT NULL,
        rating float NOT NULL,
        Num_Reviews int NOT NULL,
        Movie_ID varchar(200) NOT NULL,
        Record varchar(200) NOT NULL,
        Runtime int
        ) 
        """
# ------- Galite sukurti , kiek tik norite -------
create_table_two = f"""
        CREATE TABLE {my_database_table_name[1]} # <-- paimtas is musu lenteliu listo
        (
        {my_database_table_name[1]}Id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        Movie_Title varchar(200) NOT NULL,
        Movie_Price float NOT NULL,
        Movie_Runtime int NOT NULL
        )
        """
# ------- Galite sukurti , kiek tik norite , IR kokiu norite lenteliu -------
create_table_three = f"""
        CREATE TABLE {my_database_table_name[2]} # <-- paimtas is musu lenteliu listo
        (
        {my_database_table_name[2]}Id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        Movie_Title varchar(200) NOT NULL,
        Movie_Price float NOT NULL
        )
        """
# ------- IVYKDO DUOMENU BAZES UZDUOTIS -------
cursor.execute(create_table_one)
cursor.execute(create_table_two)
cursor.execute(create_table_three)

# ------- PRINTINA , KAD SUKURE :D -------
print(f'Table Created {my_database_table_name} : \n')

# ------- ATIDARO CSV FAILIUKA -------
with open("IMDBdata.csv") as csv_file:
    imdb_file = csv.reader(csv_file, delimiter=',') # csv.reader kad nuskaitytu csv faila. Delimeter , kad csv faile yra atskirta kableliu.
    all_values = [] # musu naujas listas , kuriame bus pridedami listai.
    none = 0 # none reiksme lygi 0
    for row in imdb_file: # for loopas ima kiekviena eilute imdb_file , kuris yra musu atidarytas csv failas
        if none > 0: # tikrina musu none reiksme
            try:
                runtime = int(row[6]) # jeigu gauname kad if reiksme none , bus False, tai except ValueError.
            except ValueError:
                runtime = 0
            value = [row[0], int(row[1]), row[2], row[3], row[4], row[5], runtime]
            print(value) # printina musu csv failo listus.
            all_values.append(value) # prideda musu listus.
        none += 1 # none reiksme pasikeicia i TRUE , todel praleidzia try ir except.

# ------- PRISKIRIAMA REIKSME , KURIOJE NURODOMA KAIP BUS IRASOMI CSV DUOMENYS  I DUOMENU BAZE -------
insert_into = """INSERT INTO IMDBdata 
              (Movie_Title,Yr_Released,rating,Num_Reviews,Movie_ID,Record,Runtime) 
              VALUES (%s, %s, %s, %s, %s, %s, %s)"""

# ------- IVYKDO DUOMENU BAZES UZDUOTIS -------
cursor.executemany(insert_into, all_values) # pirma reiksme nurodo , kaip bus ikeliami duomenys, antra reiksme ,kokie duomenys.

cursor.close()
connection.commit()
connection.close()

print("\nMySQL connection is closed")
