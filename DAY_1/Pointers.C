#include <stdio.h>

//fswatch -o Pointers.C | xargs -n1 sh -c 'gcc Pointers.C -o main'
#include <stdio.h>

int main() {
    
    // datatypes -> Pointers
    // int -> int*
    // char -> char*
    // float -> float*
    // double -> double*
    // long -> long*
    // short -> short*
    // long long -> long long *

    // struct
    // union
    // enum

    int a = 10;
    int* p = &a; // & -> get the address of a

    char ch  = 'c'; //"csafasf"
    char* cptr = &ch;


    float fp = 10.5f;
    float* fpr = &fp;


    printf("integer: %lu \n", sizeof(*p)); // 2
    printf("integer pionter: %lu \n", sizeof(p));
    //

    printf("character : %d\n", sizeof(*cptr));
    printf("character pointer: %d\n", sizeof(cptr));

    printf("float: %d\n", sizeof(*fpr));
    printf("float pointer: %d\n", sizeof(fpr));
    
    // 8gb
    // 2^3 * 2^ = 33 

    // char chrr  = 'c'; //"csafasf"
    // char* chptr = &ch;
    // int no = 66;
    // int* nptr = &no;
    // float* ffptr = (float*) nptr;

    // printf("%f", *ffptr);

    return 0;
}