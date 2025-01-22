#include <stdio.h>

//fswatch -o Pointers.C | xargs -n1 sh -c 'gcc Pointers.C -o main'
#include <stdlib.h>

int main() {
    int arr[] = {5,4,3,2,1};
    // NULL pointer
    int* nptr = NULL;
    if(nptr == NULL){
        printf("No data");
    } 

    printf("%p\n", nptr);
    printf("NULL pointer\n");


    // VOID Pointer or Generic Pointer
    printf("VOID Pointer\n");
    int num  = 1000;
    char ch = 'c';
    float flt = 7.7f;
    double db = 8.0;

    void* ptr = &num;
    printf("%d\n", *(int *)ptr);
    ptr = &ch;
    printf("%C\n", *(char *)ptr);
    ptr = &flt;
    printf("%f\n", *(float *)ptr);
    ptr = &db;
    printf("%lf\n", *(double *)ptr);

    // WILD Pointer
    printf("WILD Pointer\n");
    int* wildptr; // garbage address
    // int n; //garbage value
    printf("%p\n", wildptr);
    printf("%d\n", *wildptr);

    // // DANGLING Pointer
    printf("DANGLING Pointer\n");
    // int dangling;
    int* dangle = (int *)malloc(sizeof(int));
    *dangle = 10;
    printf("before dangle %d\n", *dangle);
    free(dangle); // memory leak
    printf("dangle %p\n", dangle);
    printf("dangle %d\n", *dangle);

    
    return 0;
}