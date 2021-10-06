#include <stdgl.h>
#include <stdio.h>

#define NC_MAX 100
#define LTIT_MAX 100
#define LA_MAX 100
#define LR_MAX 500
#define ARRAY_SEC 100
#define N_PLAYLIST 100

#define errore_apertura_file -1
#define esito_corretto 0

typedef struct t_song {
    int numero_in_playlist;
    int numero_di_riproduzione;
    char titolo_canzone[LTIT_MAX];
    char autore_canzone[LA_MAX];
}canzone;

typedef struct t_file_csv {
    canzone canzone[NC_MAX];
    int numero_canzoni;
}file_csv;

FILE* definizionePuntatoreFile();

void estrazioneAndSalvataggioDati(file_csv *struct_canzone, FILE *file_fp);

void assegnazioneNumeroRandomAndRiproduzioneCanzone(file_csv *struct_canzone);

int main(){

    file_csv file;
    FILE *fp;

    fp=definizionePuntatoreFile();

    estrazioneAndSalvataggioDati(&file, fp);

    assegnazioneNumeroRandomAndRiproduzioneCanzone(&file);

    fclose(fp);

    return esito_corretto;
}

FILE* definizionePuntatoreFile(){
    FILE *fp;
    if ((fp=fopen("playlist.csv", "r"))==NULL){
        printf("errore apertura file playlist.csv");
        return errore_apertura_file;
    }else{
        printf("corretta apertura del file playlist.csv");
    }

    return fp;
}

void estrazioneAndSalvataggioDati(file_csv *struct_canzone, FILE *file_fp){

    char array_salvataggio_temporaneo[LR_MAX];
    char *puntatore_estrazione_stringa;
    int numero_righe=0;
    int numero_canzone=0;

    for(numero_righe=0; !feof(file_fp); numero_righe++){

        fgets(array_salvataggio_temporaneo, LR_MAX, file_fp);
        puntatore_estrazione_stringa=strtok(array_salvataggio_temporaneo, ',');

        numero_canzone=ctoi(array_salvataggio_temporaneo);

        printf("%d\n", numero_canzone);

        (*struct_canzone).canzone[numero_canzone].numero_in_playlist=numero_canzone;

        puntatore_estrazione_stringa=strtok(NULL, ',');

        strcpy((*struct_canzone).canzone[numero_canzone].titolo_canzone, puntatore_estrazione_stringa);


        puntatore_estrazione_stringa=strtok(NULL, ',');

        strcpy((*struct_canzone).canzone[numero_canzone].autore_canzone, puntatore_estrazione_stringa);

        printf("%s\n", (*struct_canzone).canzone[numero_canzone].titolo_canzone);
        printf("%s\n\n", (*struct_canzone).canzone[numero_canzone].autore_canzone);
    }
    (*struct_canzone).numero_canzoni=numero_righe;
}

void assegnazioneNumeroRandomAndRiproduzioneCanzone(file_csv *struct_canzone){
    int i=0;
    int n=0;
    int numero_random=0;
    bool numero_diverso=true;

    for(int k=0; k<(*struct_canzone).numero_canzoni; k++){
        (*struct_canzone).canzone[k].numero_di_riproduzione=0;
    }

    while(i<(*struct_canzone).numero_canzoni){
        numero_random=rand()%(struct_canzone->numero_canzoni);
        for(int b=0; b<(*struct_canzone).numero_canzoni; b++){
            if(numero_random!=(*struct_canzone).canzone[b].numero_di_riproduzione){

            }else{
                numero_diverso=false;
            }
        }
        if(numero_diverso==true){
            (*struct_canzone).canzone[i].numero_di_riproduzione=numero_random;
            i++;
        }else{

        }
    }

    while(n<(*struct_canzone).numero_canzoni){
        for(int g=0; g<(*struct_canzone).numero_canzoni; g++){
            if((*struct_canzone).canzone[g].numero_di_riproduzione==n){
                printf("%s\t", (*struct_canzone).canzone[g].titolo_canzone);
                printf("%s\n\n", (*struct_canzone).canzone[g].autore_canzone);
                n++;
            }else{

            }
        }

    }

}
