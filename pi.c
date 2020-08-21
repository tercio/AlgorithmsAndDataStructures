#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static unsigned int g_seed = RAND_MAX;

// https://software.intel.com/content/www/us/en/develop/articles/fast-random-number-generator-on-the-intel-pentiumr-4-processor.html
inline int fastrand() {
	g_seed = (214013*g_seed+2531011);
	return g_seed;
	//return (g_seed>>16)&0x7FFF;
}

int main () {

    long n_runs = 5000000000;

    double fora, dentro = 0.0;
    double x,y = 0.0;

    printf ("Running: (%ld)\n",n_runs);

    while (n_runs --) {

        //x = (double)rand()/RAND_MAX*2.0-1.0;
        //y = (double)rand()/RAND_MAX*2.0-1.0;

        x = (double)fastrand()/RAND_MAX;
        y = (double)fastrand()/RAND_MAX;

        if (x*x + y*y <= 1.0)
            dentro ++;
        else
            fora ++;

        

    }

    printf ("\nPI = %.10f",(4.0*dentro/(fora+dentro)) );
        
    return 0;

}