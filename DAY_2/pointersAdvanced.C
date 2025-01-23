#include <stdio.h>
#include <stdio.h>

// command to run: gcc pointersAdvanced.C -o advanceexe && ./advanceexe

int main() {
    // // double pointer
    // printf("\ndouble pointer\n");
    // int a = 10;
    // int * ptr1 = &a;
    // int ** ptr2 = &ptr1;

    // printf("a = %d\n",a);
    // printf("%d\n",*ptr1);
    // printf("%d\n",**ptr2);

    // printf("ptr1: %lu\n",ptr1);
    // printf("ptr2: %lu\n",ptr2);

    // printf("sizeof(ptr1): %lu\n",sizeof(ptr1));
    // printf("sizeof(ptr2): %lu\n",sizeof(ptr2));

    // // multilevel pointers
    // printf("\nmultilevel pointer\n");
    // int b = 10;
    // int * mptr1 = &b;
    // int ** mptr2 = &mptr1;
    // int *** mptr3 = &mptr2;
    // printf("sizeof(mptr1): %lu\n",sizeof(mptr1));
    // printf("sizeof(mptr2): %lu\n",sizeof(mptr2));
    // printf("sizeof(mptr3): %lu\n",sizeof(mptr3));

    // //Array pointers
    // printf("\nArray pointers\n");
    // // constant pointer pointing to array address
    // int arr[] = {1,2,3,4,5};

    // // integer pointer pointing to arr address
    // int *aptr = arr;

    // // array pointer pointing to an size 5 array of integer type
    // int (*arrptr)[5] = &arr;

    // printf("arr: %lu\n",arr);
    // printf("aptr: %lu\n",aptr);
    // printf("arrptr: %lu\n",arrptr);

    // printf("sizeof(arr): %lu\n",sizeof(arr));
    // printf("sizeof(aptr): %lu\n",sizeof(aptr));
    // printf("sizeof(arrptr): %lu\n",sizeof(arrptr));


    // printf("sizeof(*aptr): %lu\n",sizeof(*aptr));
    // printf("sizeof(*arrptr): %lu\n",sizeof(*arrptr));

    // printf("before sum arr: %lu\n",arr);
    // printf("after sum arr: %lu\n",arr + 1);
    // printf("before sum aptr: %lu\n",aptr);
    // printf("after sum arrptr: %lu\n",arrptr + 1);





    //  Constant pointers

    printf("Constant pointers\n\n");
    int value = 10;
    int other_value = 20;
    
    // 1. Pointer to constant data (Data cannot change, pointer can change)
    printf("1. Pointer to Constant Data:\n");
    const int *cptr = &value;  // Read as "pointer to constant integer"
    
    printf("Initial value: %d\n", *cptr);
    // *cptr++;  
    cptr = &other_value;  
    // printf("Now points to: %d\n\n", *cptr);

    // 2. Constant pointer to mutable data (Pointer cannot change, data can change)
    printf("2. Constant Pointer to Mutable Data:\n");
    int *const const_ptr = &value;  // Read as "constant pointer to integer"
    
    printf("Original value: %d\n", *const_ptr);
    // *const_ptr = 30;  // 
    printf("Modified value: %d\n", value);
    // const_ptr = &other_value;  //
    printf("Address remains: %p\n\n", (void*)const_ptr);

    // 3. Constant pointer to constant data (Both fixed)
    printf("3. Constant Pointer to Constant Data:\n");
    const int *const const_ptr_all = &value;  // Read both consts
    
    printf("Constant value: %d\n", *const_ptr_all);
    // *const_ptr_all = 40;     
    // const_ptr_all = &other_value;  
    printf("Final address: %p\n", (void*)const_ptr_all);
   
   // 4. Constant array pointer to mutable data
   int conarr[] = {1,2,3,4,5};
   int (*const const_array_ptr)[5] = &conarr;


   eturn 0;
}