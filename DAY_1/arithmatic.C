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

    int arr[] = {1,2,3,4,5,6};
             //  0,1,2,3,4,5
             // 100,102,104,106,108,110
             // assuming int size is 2
    int * ptr1 = & arr[0]; // 1 value address: 100
    int * ptr2 = &arr[5]; // 6 th value address: 110
    long long ptrr = &arr[];
    // increment
    // ptr1++; // ptr1 = ptr1 + 1 -> 102
    // printf("%d\n", *ptr1++); // 1 * ++
    // * ptr(100) <- (ptr = ptr +1) = 102
    // //decrement
    // ptr2--;
    printf("%d\n", *--ptr2); // 5
    printf("%d\n", *ptr2--); // 5
    printf("%d\n", *ptr2); // 4
    // //addition

    // ptr+1;
    // //subtraction
    // ptr-1;

   
    return 0;
}