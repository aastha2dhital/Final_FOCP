import getpass
import codecs

# Filepath for the password file
PASSWD_FILE = 'passwd.txt'

# Encryption and decryption function (ROT-13)
def encrypt_decrypt(text):
    return codecs.encode(text, 'rot_13')

# Read the password file
def read_passwd_file():
    with open(PASSWD_FILE, 'r') as file:
        # Read and parse the password file into a list of lists
        return [line.strip().split(':') for line in file]

# Write to the password file
def write_passwd_file(data):
    with open(PASSWD_FILE, 'w') as file:
        # Write data back to the password file
        for line in data:
            file.write(':'.join(line) + '\n')

# Find a user in the password file
def find_user(username):
    users = read_passwd_file()
    for user in users:
        # Check if the given username matches any in the file
        if user[0] == username:
            return user
    return None

def check_password(stored_user, input_password):
    # Assuming the stored password is already encrypted.
    # Check if the input password matches the stored encrypted password
    encrypted_input_password = encrypt_decrypt(input_password)
    return encrypted_input_password == stored_user[2]

# Add a new user
def adduser():
    username = input("Enter new username: ")
    if find_user(username):
        print("Cannot add. Username already exists.")
        return
    
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")
    users = read_passwd_file()
    users.append([username, real_name, encrypt_decrypt(password)])
    write_passwd_file(users)
    print("User Created.")

# Delete a user
def deluser():
    users = read_passwd_file()

    username = input("Enter username: ")
    user = find_user(username)

    if user:
        password = getpass.getpass("Enter password for verification: ")
        if check_password(user, password):
            users.remove(user)
            write_passwd_file(users)
            print("User Deleted.")
        else:
            print("Password incorrect. User not deleted.")
    else:
        print("User not found.")

# Change a user's password
def passwd():
    username = input("User: ")
    user = find_user(username)
    if not user:
        print("Invalid username.")
        return

    current_password = getpass.getpass("Current Password: ")
    if user[2] != encrypt_decrypt(current_password):
        print("Invalid password.")
        return

    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm: ")
    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    user[2] = encrypt_decrypt(new_password)
    write_passwd_file(user)
    print("Password changed.")

# User login
def login():
    username = input("User: ")
    password = getpass.getpass("Password: ")
    user = find_user(username)
    if user and user[2] == encrypt_decrypt(password):
        print("Access granted.")
    else:
        print("Access denied.")

def main():
    while True:
        command = input("Enter command (adduser, deluser, passwd, login, quit): ").lower()
        if command == 'adduser':
            adduser()
        elif command == 'deluser':
            deluser()
        elif command == 'passwd':
            passwd()
        elif command == 'login':
            login()
        elif command == 'quit':
            break

if __name__ == "__main__":
    main()
