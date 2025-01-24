#include <stdio.h>
#include <stdlib.h>
// #define  struct student Student
// #define True 1
// #define False 0


typedef struct std{char name[10];int rollno;float mark;} Student;
typedef int Integer;


// struct class{
//     char name[10];
//     int classno;
//     struct student studendsinclass[3];
// };

// struct college{
//     char name[10];
//     struct class classes[3];
// };



void printstudent(Student std){
    printf("name: %s rollno : %d mark :%f\n", std.name, std.rollno, std.mark);
}

void setvalue(Student std){
    std.mark = 45.0;
}

// void setvalueint(int* x){
//     *x = 10;
// }

void setvalueaddress(Student *std){
    // both are equivalent
    // (*std).mark = 45.0;
    std->mark = 45.0;

    // std[1] is equivalent to *(std+1)
}



int main() {
    // struct student s1 = {"Rahul",20, 18.5};
    Student s1 = {"Rahul",20, 18.5};
    Integer x = 10;
    printf("x = %d\n",x);
    printstudent(s1); // "Rahul", 20, 18.5
    // setvalueaddress(&s1);
    // printstudent(s1); // "Rahul", 20, 18.5 |

    Student arrstudent[3] = 
                            {{"Ajay",20, 18.5},
                            {"Rahul",21, 39.5},
                            {"Vijay",22, 55.5}};

    for(int i = 0; i < 3; i ++){
        printstudent(arrstudent[i]);
    }

    // struct
    // struct pointer
    // array structure
    /

    // printf("%lu\n", sizeof(s1.mark));
    // printf("%lu\n", sizeof(s1.name));
    // printf("%lu\n", sizeof(s1.mark));
    // printf("%lu\n", sizeof(s1));
    
}
