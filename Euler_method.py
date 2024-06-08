#include <stdio.h>
#include <math.h>

//                                               
void analytical_solution(double t, double* x1, double* x2) {
    *x1 = 0.5 - (499.0 / 999.0) * exp(-t) - (1.0 / 1998.0) * exp(-1000.0 * t);
    *x2 = 0.5 + (500.0 / 999.0) * exp(-t) - (1.0 / 1998.0) * exp(-1000.0 * t);
}

void euler_method(double t, double h, double* x1, double* x2) {
    int num_steps = (int)(t / h) + 1;
    double x1_numeric, x2_numeric;
    double t_val = 0.0;
    int k = 0.1 / h;

    for (int i = 0; i < num_steps; i++) {
        t_val = i * h;

        if (i % k == 0) {
            printf("%.1f %.5f %.5f", t_val, *x1, *x2);
            analytical_solution(t_val, &x1_numeric, &x2_numeric);
            printf(" %.5f %.5f\n", x1_numeric, x2_numeric);
}

 double x1_dot = -501.0 * *x1 + 499.0 * *x2 + 1.0;
 double x2_dot = 500.0 * *x1 - 500.0 * *x2;

*x1 += h * x1_dot;
*x2 += h * x2_dot;
}
}

int main() {
    double x1_analytical = 0, x2_analytical = 0;
    double t = 1.0;
    double h = 0.001;

 //                      
euler_method(t, h, &x1_analytical, &x2_analytical);
printf("t_val\teiler_1\teiler_2\tanal_1\tanal_2\n");

return 0;
}
