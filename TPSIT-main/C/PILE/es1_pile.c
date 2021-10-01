#include <stdio.h>
#include <stdlib.h>

int is_empty(struct El *head) {
    if(head == NULL) {
        return 1;
    }
    else {
        return 0;
    }
}

void enqueue(struct El **head, struct El** tail, struct El *element) {
    if(is_empty(*head)) {
        *head = element;
    }
    else {
        *tail->next = element;
    }

    *tail = element;
    element->next = NULL;
}

struct El * dequeue(struct El **head, struct El **tail) {
    struct El *ret = *head;

    if(is_empty(*head)) {
        return NULL;
    }
    else {
        *head = ret->next;
    }
    if(*head == NULL) {
        *tail = NULL;
    }

    return ret;
}

int main() {
    int n;


    printf("Inserisci un numero : ");
    scanf("%d", n);
}