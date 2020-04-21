// For domain interval [3pi/2, 9pi/2], solve for sin(x) = 0.65.

#include <stdio.h>
#include <math.h>
#define PI 3.14159265

int main(void) {
    for (double x = 3*PI/2; x <= 9*PI/2; x += .02) {
        double y = sin(x);
        if (y >= 0.645 && y <= 0.654) {
            printf("%.2lf\n", x);
        }
    }
        

    return 0;
}
