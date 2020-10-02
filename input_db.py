import getpass # tesiog nerodo tekstine israiska passwordo ,kuri rasote terminale.

host = input("Please enter your MySQL host : ") # example host = localhost
user = input("Please enter your MySQL user : ") # example user = root
password = getpass.getpass("Please enter your MySQL password: ") # example password = 1234
my_database_name = input("Please enter your MySQL database name : ") # example database_name = imdbData