import sqlite3
import random
import string

def generate_password():

    print("Please answer the questions with 'Y' for Yes or 'N' for No.")
    number_check = input("Would you like to include numbers? ").strip().upper()
    lowercase_check = input("Would you like to include lowercase letters? ").strip().upper()
    uppercase_check = input("Would you like to include uppercase letters? ").strip().upper()
    punctuation_check = input("Would you like to include punctuation characters? ").strip().upper()

    final_str=""

    if number_check == "Y":
        final_str += string.digits

    if lowercase_check == "Y":
        final_str += string.ascii_lowercase

    if uppercase_check == "Y":
        final_str += string.ascii_uppercase

    if punctuation_check == "Y":
        final_str += string.punctuation

    password_length = int(input("What should be the length of the password?"))

    final_password=""

    for i in range(0, password_length):
        index = random.randint(0, len(final_str))
        final_password +=final_str[index]
    print("Your final password: {}".format(final_password))

    return final_password


class Password():
    def __init__(self, platform, short_name, password):
        self.platform = platform
        self.short_name = short_name
        self.password = password

    def __str__(self):
        return "Platform name: {}\nShort name: {}\nPassword: {}".format(self.platform, self.short_name, self.password)


class Storage():
    def __init__(self):
        self.establish_connection()

    def establish_connection(self):
        self.connection = sqlite3.connect("storage.db")
        self.cursor = self.connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS passwords(platform TEXT,short_name TEXT,password TEXT)"
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def add_password(self, password):
        query = "INSERT INTO passwords VALUES(?,?,?)"

        self.cursor.execute(query, (password.platform, password.short_name, password.password))

        self.connection.commit()

    def search_password_full(self, platform):
        query = "SELECT * FROM passwords WHERE platform=?"
        self.cursor.execute(query, (platform,))
        passwords = self.cursor.fetchall()
        if (len(passwords) == 0):
            print("There is no such password.")
        else:
            password_result = Password(passwords[0][0], passwords[0][1], passwords[0][2], )
            print(password_result)
    
    def search_password_short(self, short_name):
        query = "SELECT * FROM passwords WHERE short_name=?"
        self.cursor.execute(query, (short_name,))
        passwords = self.cursor.fetchall()
        if (len(passwords) == 0):
            print("There is no such password.")
        else:
            password_result = Password(passwords[0][0], passwords[0][1], passwords[0][2], )
            print(password_result)