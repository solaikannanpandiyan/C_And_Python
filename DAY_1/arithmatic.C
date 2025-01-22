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

    int arr[] = {1,  2,  3,  4,  5,  6};
             //  0,  1,  2,  3,  4,  5
             // 100,102,104,106,108,110
             // assuming int size is 2
    int * ptr1 = & arr[0]; // 1 value address: 100
    int * ptr2 = &arr[5]; // 6 th value address: 110

    // increment
    // ptr1++; // ptr1 = ptr1 + 1 -> 102
    // printf("%d\n", *ptr1++); // 1 * ++
    // * ptr(100) <- (ptr = ptr +1) = 102

    // //decrement
    // ptr2--;
    // printf("%d\n", *--ptr2); // 5
    // printf("%d\n", *ptr2--); // 5
    // printf("%d\n", *ptr2); // 4

    // //addition
    printf("%u \n",ptr1); // 4
    ptr1 = ptr1 + 3; 
    // 84(address) + 4(size of data type in machine) * 3 (no to be added) = next address
    printf("%u",ptr1);
    // printf("%d\n",*ptr1);
    

    // //subtraction
    // ptr-1;
     printf("%u \n",ptr2); // 4
    ptr2 = ptr2 - 3; 
    // 84(address) + 4(size of data type in machine) * 3 (no to be added) = next address
    printf("%u",ptr2);

    // subtraction of pointers
    printf("%d", ptr2 - ptr1); 
    // 110 - 100 = 10
    // 10 / 2(size of int) = 5
   
    return 0;
}