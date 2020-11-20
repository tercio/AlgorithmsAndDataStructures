#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void swap (int *a, int x, int y) {
    int tmp = a[x];
    a[x] = a[y];
    a[y] = tmp;
}

int partition(int *a, int l, int u) {
        // partition
    int m = l;
    
    for (int i=l+1; i <= u; i++) {

        if (a[i] < a[l]) {
            swap (a,++m,i);
        }

    }

    swap (a,l,m);

    return m;
}

void myqsort (int *a,int l, int u) {

    if (l >= u) return;

    int m = partition(a,l,u);

    myqsort (a,l,m-1);
    myqsort (a,m+1,u);

}


int main(){

    int a[] = {55,41,59,26,53,58,97,93};
    int n = 8;

    printf ("before: ");
    for (int i=0; i<n ; i++){
        printf ("%d ",a[i]);
    }
    printf ("\n");

    myqsort (a,0,n-1);

    printf ("after:  ");
    for (int i=0; i<n ; i++){
        printf ("%d ",a[i]);
    }
    printf ("\n");

    return 0;
}