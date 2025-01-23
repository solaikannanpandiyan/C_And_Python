#include <stdio.h>
#include <stdio.h>

// command to run: gcc pointersAdvanced.C -o advanceexe && ./advanceexe
// pass by value -> but data is the value
void swapbyvalue(int a, int b){
    int temp = a;
    a = b;
    b = temp;
}

// value by value -> but address is the value
void swapbypointer(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void swaparr(int arr[]){
    int temp = arr[0];
    arr[0] = arr[4];
    arr[4] = temp;
}

int main() {
    int a = 10;
    int b = 20;
    int array[5] = {1,2,3,4,5}; 
    printf("swap by value\n");
    printf("a = %d b =%d\n", a, b); // a = 10 b =20
    swapbyvalue(a, b);
    printf("a = %d b =%d\n", a, b); // a = 20 b = 10 | 

    printf("swap by pointer\n");
    printf("a = %d b =%d\n", a, b);
    swapbypointer(&a, &b); // 100 200
    printf("a = %d b =%d\n", a, b);

    printf("\n");
    for(int i = 0; i < 5; i++ ){
        printf("%d ", array[i]);
    }
    printf("\n");
    swaparr(array);
    for(int i = 0; i < 5; i++ ){
        printf("%d ", array[i]); // 5 2 3 4 1
    }


    

}