#include <stdio.h>
#include <stdlib.h>


int mybsearch (int *data,int value,int l,int r) {


    if (l > r) return 0;

    int m = (l + r) / 2;

    if (value == data[m]) return 1;
    else if (value < data[m]) return mybsearch(data,value,l,m);
    else return mybsearch(data,value,m+1,r);     

}


int main (int argc, char *argv[]) {

    int data[] = {0,1,2,3,4,5,6,7,8,9};

    if (argc != 2) {
        printf ("uso:%s value\n",argv[0]);
        exit (0);
    }

    int value = atoi(argv[1]);

    printf ("o valor %d %s foi encontrado\n",value,mybsearch(data,value,0,9) == 0 ? "não" : "");

    return 0;
}