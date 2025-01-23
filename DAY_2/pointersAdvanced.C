#include <stdio.h>

//fswatch -o Pointers.C | xargs -n1 sh -c 'gcc Pointers.C -o main'
#include <stdio.h>

int main() {
    // double pointer
    int a = 10;
    int * ptr1 = &a;
    int ** ptr2 = &ptr1;

    printf("a = %d\n",a);
    printf("%d\n",*ptr);
    printf("%d\n",**ptr2);

    printf("ptr1: %lu\n",ptr1);
    printf("ptr2: %lu\n",ptr2);

    printf("sizeof(ptr1): %lu\n",sizeof(ptr1));
    printf("sizeof(ptr2): %lu\n",sizeof(ptr2));

    // multilevel pointers

    int arr[] = {5,4,3,2,1};
    int a = 10;
    int * mptr1 = &a;
    int ** mptr2 = &mptr1;
    int *** mptr3 = &mptr2
    printf("sizeof(mptr1): %lu\n",sizeof(mptr1));
    printf("sizeof(mptr2): %lu\n",sizeof(mptr2));
    printf("sizeof(mptr3): %lu\n",sizeof(mptr3));

    // multilevel pointers
    
    
    return 0;
}