#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define er_app -1
#define errore_lettura_nucleotidi -2
#define pr_ok 0

#define numero_max_caratteri_per_riga 300
#define numero_max_caratteri_per_parte_di_riga 100
#define numero_parti_per_riga 6
#define numero_caratteri_per_parte_di_riga 10
#define numero_max_caratteri_vettore_secondario 10

bool numeroAndTipoNeuclotidiTrovati(int *a, int *t, int *c, int *g, char *riga);

int main(){

    int numero_nucleotidi_a=0;
    int numero_nucleotidi_t=0;
    int numero_nucleotidi_c=0;
    int numero_nucleotidi_g=0;

    char riga[numero_max_caratteri_per_riga];

    FILE *file_rna;

    if ((file_rna=fopen("rna.txt", "r"))==NULL){    
        printf("Errore File\n");
        return er_app;
    }

    fgets(riga, numero_max_caratteri_per_riga, file_rna);

    while(!feof(file_rna)) {    
        if(numeroAndTipoNeuclotidiTrovati(&numero_nucleotidi_a, &numero_nucleotidi_t, &numero_nucleotidi_c, &numero_nucleotidi_g, riga)==false){
            return errore_lettura_nucleotidi;
        }
    }

    printf("Numero di nucleotidi adenina: %d\n", numero_nucleotidi_a);
    printf("Numero di nucleotidi timina: %d\n", numero_nucleotidi_t);
    printf("Numero di nucleotidi citosina: %d\n", numero_nucleotidi_c);
    printf("Numero di nucleotidi guanina: %d\n\n", numero_nucleotidi_g);

    return pr_ok;
}

bool numeroAndTipoNeuclotidiTrovati(int *a, int *t, int *c, int *g, char *riga){    
    char *parte_di_riga;
    char vettore_secondario[numero_max_caratteri_vettore_secondario];

    parte_di_riga=strtok(riga, ' ');   

    for(int i=0; i<numero_parti_per_riga; i++){   
        parte_di_riga=strtok(NULL, ' ');  
        vettore_secondario=strdup(parte_di_riga);   
        for(int k=0; k<numero_caratteri_per_parte_di_riga; k++){   
            switch (*(vettore_secondario+k)){
                case 'a':
                (*a)++;
                break;
                case 't':
                (*t)++;
                break;
                case 'c':
                (*c)++;
                break;
                case 'g':
                (*g)++;
                break;
                default:
                return false;
                break;
            }
        }
    }

    return true;

}