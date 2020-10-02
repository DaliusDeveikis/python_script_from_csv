import getpass # tesiog nerodo passwordo ,kuri rasote terminale.

host = input("Please enter your MySQL host : ")
user = input("Please enter your MySQL user : ")
password = getpass.getpass("Please enter your MySQL password: ")
my_database_name = input("Please enter your MySQL database name : ")