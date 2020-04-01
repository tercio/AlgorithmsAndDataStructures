// Substring Search Brute Force algorithm
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main (int argc, char *argv[]){

    if (argc != 3) {
        printf ("uso:%s <string> <pattern>\n",argv[0]);
        exit(0);
    }

    int N = strlen(argv[1]);
    int M = strlen(argv[2]);
    int found = 0;
    int i,j;

    for (i=0; i <= N-M; i++) {

        for (j=0; j < M; j++) {
            if (argv[1][i+j] != argv[2][j])
                break;
        }
        if (j == M)
            found = 1;
    }

    printf ("O pattern: \"%s\" %s encontrada na string: \"%s\"\n",argv[2],(found == 1)?"foi":"não foi",argv[1]); 


    return 0;
}