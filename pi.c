#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main () {

    long n_runs = 5000000000;

    double fora, dentro = 0.0;
    double x,y = 0.0;

    printf ("Running: (%ld)\n",n_runs);

    while (n_runs --) {

        x = (double)rand()/RAND_MAX*2.0-1.0;
        y = (double)rand()/RAND_MAX*2.0-1.0;

        if (x*x + y*y <= 1.0)
            dentro ++;
        else
            fora ++;

        

    }

    printf ("\nPI = %.10f",(4.0*dentro/(fora+dentro)) );
        
    return 0;

}