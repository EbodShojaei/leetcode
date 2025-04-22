// see https://leetcode.com/problems/powx-n/
// Python just uses ** operator
// C implementation of pow(x, n) uses binary exponentiation
// e.g., 2^7
//      (2 * 2) * (2 * 2) * (2 * 2) * 2
//      (4 * 4) * (4 * 2)
//      16 * 8
//      128
//      2^7 = 128

#include <stdio.h>
#include <stdlib.h>

double myPow(double x, int n) {
    double result = 1.0;
    long long abs_n = n;

    if (n < 0) {
        x = 1.0 / x;
        abs_n = -abs_n;
    }

    while (abs_n > 0) {
        printf("x: %f, abs_n: %lld, result: %f\n", x, abs_n, result);
        if (abs_n % 2 == 1) {
            result *= x;
        }
        x *= x;
        abs_n /= 2;
    };

    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <base> <exponent>\n", argv[0]);
        return 1;
    }
    double x = atof(argv[1]);
    int n = atoi(argv[2]);
    printf("myPow(%f, %d) = %f\n", x, n, myPow(x, n));

    return 0;
}
