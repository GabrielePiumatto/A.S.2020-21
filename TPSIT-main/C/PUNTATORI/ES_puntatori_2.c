#include <stdio.h>

int main(){
    int *p;
    int n=0;

    scanfInt("inserire grandezza array: ", &n);
    
    p = (int *)malloc(sizeof(int)*n);  

    for(int i=0; i<n; i++){  
        scanfInt("Inserisci un numero: ", (p+i));
    }

    for(int i=0; i<n; i++){ 
        printf("%d\n", *(p+i));
    }


    free(p);
    
    return 0;
}