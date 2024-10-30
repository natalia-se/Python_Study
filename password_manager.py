from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


masster_pwd = input("What is the master password? ")
key = load_key() + masster_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, " Password:", fer.decrypt(password.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:

    mode = input("Would you like to view existing passwords or add new one? (add/ view) ")
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode =="view":
        view()

    else:
        print("Invalid mode")
        continue