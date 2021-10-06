//Esercizio per il calcolo dei contagi 

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define max_numero_giorni_in_cui_tutti_possono_essere_contagiati 500

int main() {
    int N=0, numero_giorno=0;
    float numero_contagiati=1, R=0;

    float contagi_per_giorno[max_numero_giorni_in_cui_tutti_possono_essere_contagiati];

    printf("Inserisci il numero di persone che contagia una sola persona: ");
    scanf("%f", &R);
    printf("\n");

    printf("Inserisci il numero di persone da contagiare: ");
    scanf("%d", &N);
    printf("\n");

    while(numero_contagiati<N) {    
        contagi_per_giorno[numero_giorno]=numero_contagiati;
        printf("Nel giorno %d, il numero di contagiati e' : %d\n", numero_giorno, (int)contagi_per_giorno[numero_giorno]);
        numero_contagiati=pow(R,numero_giorno);
        numero_giorno++;
    }

    if(numero_contagiati==N) {     
        numero_giorno--;
    }

    else {   
    contagi_per_giorno[numero_giorno]=numero_contagiati;
    }

    float differenza_contagiati_tra_ultimo_e_penultimo_giorno = contagi_per_giorno[numero_giorno] - contagi_per_giorno[numero_giorno-1];
    float var = (float)N - contagi_per_giorno[numero_giorno-1];

    int numero_ore_per_completare_il_contagio_nell_ultimo_giorno = (24*var)/differenza_contagiati_tra_ultimo_e_penultimo_giorno;

    printf("Il contagio è avvenuto in %d giorni/o e %d ore/a\n", numero_giorno++, numero_ore_per_completare_il_contagio_nell_ultimo_giorno);

    
    return 0;
}