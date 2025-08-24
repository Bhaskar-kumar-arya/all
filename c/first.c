#include <stdio.h>
#include <stdlib.h>

int* getPtr() {
    int *p = (int*) malloc(sizeof(int));
    *p = 25;
    return p;
}

int main() {
    int *q = getPtr();
    printf("%d",*q);
    free(q);
    return 0;
}
