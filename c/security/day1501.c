#include <stdio.h>

struct student
{
    int id;
    int age;
    char *name;
};


int main(int argc, char *argv[])
{

    struct student stu;
    struct student* pstu;

    pstu = &stu;

    pstu->id = 1;
    pstu->age = 21;
    pstu->name = "Dooley";
    
    printf("id : %d\n", stu.id);
    printf("age : %d\n", stu.age);
    printf("name : %s\n", stu.name);
    
    return 0;
}
