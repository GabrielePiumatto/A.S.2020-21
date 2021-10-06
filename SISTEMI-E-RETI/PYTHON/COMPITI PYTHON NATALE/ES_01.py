import random
import string


def main():
    print("Inserisci 1 per password corta o 2 per password lunga")
    n = int(input("Inserisci un numero: "))

    if(n==1):

        password = ""
        for i in range(8):
            password = password + random.choice(string.ascii_uppercase + string.digits)

        print(f"La password generata è : {password}")

    if(n==2):

        password = ""
        for i in range(20):
            password = password + random.choice(string.ascii_uppercase + string.digits)

        print(f"La password generata è : {password}")

if __name__ == "__main__":
    main()