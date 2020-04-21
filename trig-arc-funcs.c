#include <stdio.h>
#include <math.h>

int main(void) {

    // asin() returns a double in the interval of [   -1,    +1] radians (DOMAIN)
    // asin() returns a double in the interval of [-pi/2, +pi/2] radians (RANGE)
    for (double i = -1; i <= 1; i += .2) {
        printf("%lf\n", asin(i));
    }
    printf("\n");

    // acos() accepts a double in the interval of [-1, +1] radians (DOMAIN)
    // acos() returns a double in the interval of [ 0, pi] radians (RANGE)
    for (double i = -1; i <= 1; i += .2) {
        printf("%lf\n", asin(i));
    }
    printf("\n");

    // atan() accepts double in the interval of [   -1,   +1] radians (DOMAIN)
    // atan() returns double in the interval of [-pi/2, pi/2] radians (RANGE)
    for (double i = -1; i<= 1; i += .2) {
        printf("%lf\n", atan(i));
    }
    printf("\n");

    return 0;
}
