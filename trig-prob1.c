// For domain [-2pi, 2pi], which x values of cos(x) equal 1, and which equal -1?
// URL: https://www.khanacademy.org/math/trigonometry/trig-equations-and-identities/basic-sinusoidal-equations/v/we-graph-of-cosine-function

#include <stdio.h>
#include <math.h>

int main(void) {

    // starting at -2pi, until 2pi, incrementing by pi/4... 
    for (double x = -2*(M_PI); x <= 2*M_PI; x += (M_PI)/4) {

        // if result == 1, say so
        if (cos(x) == 1) {
            printf("cos(%.2lfPI) = %.2lf\n", x/M_PI, cos(x));
        }
        // else if result == -1, say so 
        else if (cos(x) == -1) {
            printf("cos(%.2lfPI) = %.2lf\n", x/M_PI, cos(x));
        }
    }

    // return
    return 0;
}
