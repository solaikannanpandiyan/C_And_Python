#include <stdio.h>

//fswatch -o Pointers.C | xargs -n1 sh -c 'gcc Pointers.C -o main'
#include <stdio.h>

int main() {
    int arr[] = {5,4,3,2,1};
    // int k =10;
    int* arrptr = arr;
    printf("arr : %u \n", arr);
    printf("arrptr : %u\n", arrptr);
    // https://upaste.de/JqC

    for(int i = 0;i<5;i++){
        // printf("%d ",arr[i]);
        printf("%d ",*(arr+i));
    }
    printf("\n");

    for(int i = 0;i<5;i++){
        // printf("%d ",arrptr[i]);
        printf("%d ",*(arrptr+i));
    }
    // printf("\n");
    printf("\n");
    printf("%lu\n", sizeof(arr)); // 20
    // int -> 4 bytes
    // ptr -> 8 bytes | 8 * 5 =  40
    printf("%lu\n", sizeof(arrptr)); // 8
    return 0;
}