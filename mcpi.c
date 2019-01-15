/*
 * c code for computing pi using the monte carlo method
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rand_unit() {
    /* Return a random number between zero and one exclusive */
    return (double)rand() / (double)RAND_MAX;  /* declare outside? */
}
double calc_pi(int n) {
    /*
     * Calculate pi using n random samples
     */
    int itr, s=0;
    double x, y;

    for (itr=0;itr<n;itr++) {
        x = rand_unit();
        y = rand_unit();
        if (sqrt(x * x + y * y) <= 1) s++;
    }
    return 4.0 * (double)s / (double)n;
}

int main(){
    int n;
    int samples[4] = {
        1000, 10000, 1000000, 1000000,
    };

    /* initialize */

    srand(time(NULL));

    for (n=0;n<4;n++) {
        printf("Pi with %d samples: %f\n", samples[n], calc_pi(samples[n]));
    }
    return 0;
}
