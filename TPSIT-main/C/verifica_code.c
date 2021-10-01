#include <stdio.h>  //dichiarazione librerie
#include <stdlib.h>

typedef struct carta{   //creazione carta
    char seme;          //seme sottoforma di char
    int valore;         //numero della carta
    struct carta* next;
}Carta;

//funzione per aggiungere carte = equivale alla push
void enqueue(Carta **head, Carta **tail,Carta *element){
	if(*head==NULL){    //se la testa è vuota
		*head=element;  //inserirci elemento dentro
	}
	else {
        (*tail)->next=element;  //trasferire elemento
    }
	
	*tail=element;
	element->next=NULL; //elemento si svuota e l'inoput è salvato in memoria
}

//funzione per rimuovere carte = equivale alla pop
Carta* dequeue(Carta **head,Carta **tail){
    Carta *ret=*head;

	if(*head == NULL){  //se la testa è vuota
		return NULL;    //ritorna nullo
	}
	else
		(*head)=ret->next;  
	if(*head == NULL)   //se head è uguale a NULL
		*tail=NULL;     //anche tail è null
	return ret; //quest'area di memoria viene "staccata" dalla coda
}

int main(){
    Carta *head;    //crea un insieme di puntatori a HEAD
    Carta *tail;    //crea un insieme di puntatori a TAIL
    Carta *element; //crea un insieme di puntatori a ELEMENT
    //dichiarazione variabili
    int val;
    char s;

    //head e tail puntano a NULL
    head=NULL;
    tail=NULL;
    element=(Carta*)malloc(52*sizeof(Carta)); //allocazione dinamica di carta
                                              //salvata su element
    if(element==NULL) { //gestione degli errori
        printf("Allocazione Fallita\n");
        exit(0);
    }   

    for(int i=0; i<52; i++) { //creazione mazzo
        while(i<13) {   //insieme carte picche
            val = i+1;
            s = "picche";
            scanf("%d", &val);  //salvataggio nelle variabili
            scanf("%c", &s);
        }
        while(i=13 && i<26) {   //insieme carte fiori
            val = (i-13)+1;
            s = "fiori";
            scanf("%d", &val);  //salvataggio nelle variabili
            scanf("%c", &s);
        }
        while(i=26 && i<39) {   //insieme carte quadri
            val = (i-13*2)+1;
            s = "quadri";
            scanf("%d", &val);  //salvataggio nelle variabili
            scanf("%c", &s);
        }
        while(i=39 && i<52) {   //insieme carte cuori
            val = (i-13*3)+1;
            s = "cuori";
            scanf("%d", &val);  //salvataggio nelle variabili
            scanf("%c", &s);
        }
    }

    free(element);  //libera element per la pop

    return 0;   //fine programma
}