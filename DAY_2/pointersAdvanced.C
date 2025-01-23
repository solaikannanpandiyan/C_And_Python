#include <stdio.h>

//fswatch -o Pointers.C | xargs -n1 sh -c 'gcc Pointers.C -o main'
#include <stdio.h>

int main() {
    // double pointer
    printf("\ndouble pointer\n");
    int a = 10;
    int * ptr1 = &a;
    int ** ptr2 = &ptr1;

    printf("a = %d\n",a);
    printf("%d\n",*ptr1);
    printf("%d\n",**ptr2);

    printf("ptr1: %lu\n",ptr1);
    printf("ptr2: %lu\n",ptr2);

    printf("sizeof(ptr1): %lu\n",sizeof(ptr1));
    printf("sizeof(ptr2): %lu\n",sizeof(ptr2));

    // multilevel pointers
    printf("\nmultilevel pointer\n");
    int b = 10;
    int * mptr1 = &b;
    int ** mptr2 = &mptr1;
    int *** mptr3 = &mptr2;
    printf("sizeof(mptr1): %lu\n",sizeof(mptr1));
    printf("sizeof(mptr2): %lu\n",sizeof(mptr2));
    printf("sizeof(mptr3): %lu\n",sizeof(mptr3));

    //Array pointers
    printf("\nArray pointers\n");
    // constant pointer pointing to array address
    int arr[] = {1,2,3,4,5};
    
    // integer pointer pointing to arr address
    int *aptr = arr;

    // array pointer pointing to an size 5 array of integer type
    int (*arrptr)[5] = &arr;

    printf("arr: %lu\n",arr);
    printf("aptr: %lu\n",aptr);
    printf("arrptr: %lu\n",arrptr);

    printf("sizeof(arr): %lu\n",sizeof(arr));
    printf("sizeof(aptr): %lu\n",sizeof(aptr));
    printf("sizeof(arrptr): %lu\n",sizeof(arrptr));


    printf("sizeof(*aptr): %lu\n",sizeof(*aptr));
    printf("sizeof(*arrptr): %lu\n",sizeof(*arrptr));

    printf("before sum arr: %lu\n",arr);
    printf("after sum arr: %lu\n",arr + 1);
    printf("before sum aptr: %lu\n",aptr);
    printf("after sum arrptr: %lu\n",arrptr + 1);

    
    return 0;
}