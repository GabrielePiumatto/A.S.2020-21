//Esercizio per capire il funzionamento di indirizzi e puntatori

#include <stdlib.h>
#include <stdio.h>

int main() {

    int *pi;
    int a=5, b;

    pi = &a;
    b= *pi;

    *pi = 9;

    printf("*pi = %d\n", *pi);
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;

}