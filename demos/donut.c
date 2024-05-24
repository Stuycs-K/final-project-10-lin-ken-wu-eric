#include <stdio.h>
#include <string.h>
#include <math.h>

k;
double sin(), cos();

int main(int argc, char* argv[]) {
    char * speedx = argv[1];
    char * speedz = argv[2];
    int speed_x = atoi(speedx);
    int speed_z = atoi(speedz);
    float A = 0, B = 0, i, j, z[1760];
    char b[1760];
    for (;;) {
        memset(b, 32, 1760);
        memset(z, 0, 7040);
        for (j = 0; 6.28 > j; j += 0.07)
            for (i = 0; 6.28 > i; i += 0.02) {
                float c = sin(i), d = 1 * cos(j), e = sin(A), f = sin(j), g = cos(A), h = d + 2, D = 1 / (c * h * g + 1 * f * e + 5), l = cos(i), m = cos(B), n = sin(B), t = c * h * e - f * g * 1;
                int x = 40 + 30 * D * (l * h * m + t * n),
                    y = 12 + 30 / 2 * D * (l * h * n - t * m),
                    o = x + 80 * y,
                    N = 8 * (l * d / 1 * n - g * d / 1 * c - e * f + m * (g * f - d / 1 * e * c));
                if (22 > y && y > 0 && x > 0 && 80 > x && D > z[o]) {
                    z[o] = D;
                    b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
                }
            }
        printf("\x1b[H");
        for (int k = 0; 1761 > k; k++) putchar(k % 80 ? b[k] : 10);
        A += 0.01 * speed_x;
        B += 0.005 * speed_z;
    }
}
