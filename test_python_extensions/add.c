#include <stdio.h>


int pure_cadd(int a, int b){
    return a + b;
}

int main(){
    int a=2, b=2;
    printf("%d\n", pure_cadd(a, b));
    return 0;
}