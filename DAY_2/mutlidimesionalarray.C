#include <stdio.h>
#include <stdio.h>

// command to run: gcc pointersAdvanced.C -o advanceexe && ./advanceexe

int main() {
    int arr[][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
    // 1    2   3   4   5   6    7   8    9
    // 100  102 104 106 108 110  112 114  116
    int *ptr = &arr[0][0]; 
    // int *ptr = arr
    // int (*ptr2d)[3][3] = &arr; 

     printf("\nUsing *ptr:\n");
    for (int i = 0; i < 9; i++) {
        printf("%d ", ptr[i]);
        if ( (i + 1) % 3 == 0)
            printf("\n");
    }

    int (*ptrrr)[3] = arr;
    ptrrr[2][0]);
    printf("\nUsing (*ptrrr)[3]:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", ptrrr[i][j]);
        }
        printf("\n");
    }

    printf("\nUsing arr :\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;

}