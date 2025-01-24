#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("MALLOC\n");
    int *a = (int*)malloc(2*sizeof(int)); // 8 bytes
    if(a == NULL){
        printf("%p\n", a);
        printf("unable to allocate memory");
        exit(1);
    }else{
        printf("memory allocated");
    }

    printf("%lu\n", a); //address
    printf("%lu\n",sizeof(a)); // 8
    printf("%d\n", a[0]); //GV
    printf("%d\n", a[1]); //GV
    printf("\n\n");

    printf("CALLOC\n");
    int *b = (int*)calloc(2,sizeof(int));
    printf("%lu\n", b);
    printf("%d\n", b[0]);
    printf("%d\n", b[1]);
    printf("\n\n");

    printf("REALLOC\n");
    int *r = (int*)realloc(a,1000*sizeof(int));
    printf("%lu\n", r);
    printf("%d\n", r[0]);
    printf("%d\n", r[1]);
    printf("%d\n", r[3]);
    printf("%d\n", r[4]);
    printf("\n\n");

    return 1;

}