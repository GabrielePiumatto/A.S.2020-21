#include <stdio.h>
#include <stdlib.h>

typedef struct S_El {
int valore;
struct S_El* next;
} El;

void push(El* head, int n);
void stampaLista(El* head);

int main() {
    int n=0;
    El* head;
    El* l;
    head=NULL; 

    while(n>=0) {

        printf("Inserisci un naturale o -1 per terminare: ");
        scanf("%d",&n);

        if(n>=0){

            if(head==NULL) { 
                head = (El*) malloc(sizeof(El));
                l = head;
                l->valore=n;
            }
            else{
                push(head, n);
            }

        }
    }

    printf("numeri inseriti: \n");
    stampaLista(head);

    printf("\n");
    return 0;
}


void push(El* head, int n){
        
    while(head->next!=NULL){
        head = head->next;
    }
        head->next = (El*) malloc(sizeof(El));
        head->next->valore=n;
        head->next->next = NULL;

}

void stampaLista(El* head){
    while(head!=NULL){
        printf("%d - %p \n",head->valore, head->next);
        head = head->next; 
    }
}