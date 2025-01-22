#include <stdio.h>

//fswatch -o Pointers.C | xargs -n1 sh -c 'gcc Pointers.C -o main'
#include <stdio.h>

void swap(int* first, int* second){
    //     10   ,   5
    //    100   , 200
    int temp = *first;
    *first = *second;
    //     5   ,   5
    //    100   , 200
    *second = temp;
    //     5   ,   10
    //    100   , 200
}

int main() {
    int arr[] = {5,4,3,2,1};
    for(int i = 0; i<5;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    swap(&arr[0],&arr[4]);
    for(int i = 0; i<5;i++){
        printf("%d ",arr[i]);
    }
    return 0;
}