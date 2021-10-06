import random

esadecimale = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def main():
    for indice in range(12):
        if (indice%2 == 0 and indice != 0):
            print(':',end='')
        print(random.choice(esadecimale),end='')

if __name__ == "__main__":
    main()