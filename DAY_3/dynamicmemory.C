#include <stdio.h>
#include <stdlib.h>

void test(){
    int a = 10;
}

int main() {
    // printf("MALLOC\n");
    // // 10000
    // // 10000
    
    // int *a = (int*)malloc(2*sizeof(int)); // 8 bytes
    // if(a == NULL){
    //     printf("%p\n", a);
    //     printf("unable to allocate memory");
    //     exit(1);
    // }else{
    //     printf("memory allocated");
    // }

    // printf("%lu\n", a); //address
    // printf("%lu\n",sizeof(a)); // 8
    // printf("%d\n", a[0]); //GV
    // printf("%d\n", a[1]); //GV
    // printf("\n\n");
    // // free(a);

    // printf("CALLOC\n");
    // int *b = (int*)calloc(2,sizeof(int));
    // printf("%lu\n", b);
    // printf("%d\n", b[0]);
    // printf("%d\n", b[1]);
    // printf("\n\n");

    // printf("REALLOC\n");
    // int *r = (int*)realloc(a,1000*sizeof(int));
    // printf("%lu\n", r);
    // printf("%d\n", r[0]);
    // printf("%d\n", r[1]);
    // printf("%d\n", r[3]);
    // printf("%d\n", r[4]);
    // printf("\n\n");

    // free
    free(a);
    //used to free the memory so it can be reused 
    //while calling malloc or realloc again

    // memory leak
    // printf("MEMORY LEAK");
    // int *a;
    // for( int i = 0; i < 1000000; i++){
    //     a = (int*)malloc(2*10000); // 8 bytes
    //     if(a == NULL){
    //         printf("%p\n", a);
    //         printf("unable to allocate memory");
    //         exit(1);

            
    //     }else{
    //         printf("memory allocated of size 200 bytes\n");
    //     }
    //     free(a);
    // }

    return 1;

}