#include <stdio.h>
#include <gmp.h>

#define PRECISION 10000
#define N_TERMS 10

void chudnovsky_pi(mpf_t pi) {
    mpf_t C, M, L, X, K, S, temp1, temp2;
    mpf_inits(C, M, L, X, K, S, temp1, temp2, NULL);

    // 初始化常数
    mpf_set_ui(M, 1);
    mpf_set_ui(L, 13591409);
    mpf_set_ui(X, 1);
    mpf_set_ui(K, 6);
    mpf_set_ui(S, 13591409);

    // 计算 C
    mpf_set_ui(temp1, 10005);
    mpf_sqrt(temp1, temp1);
    mpf_mul_ui(C, temp1, 426880);

    for (int i = 1; i < N_TERMS; i++) {
        // 计算 M
        mpf_set_ui(temp1, K);
        mpf_pow_ui(temp1, temp1, 3);
        mpf_mul_ui(temp2, K, 16);
        mpf_sub(temp1, temp1, temp2);
        mpf_mul(M, M, temp1);
        mpf_set_ui(temp1, i);
        mpf_pow_ui(temp1, temp1, 3);
        mpf_div(M, M, temp1);

        // 计算 L
        mpf_add_ui(L, L, 545140134);

        // 计算 X
        mpf_mul_ui(X, X, -262537412640768000);

        // 计算 S
        mpf_mul(temp1, M, L);
        mpf_div(temp1, temp1, X);
        mpf_add(S, S, temp1);

        // 计算 K
        mpf_add_ui(K, K, 12);
    }

    // 计算圆周率
    mpf_div(pi, C, S);

    mpf_clears(C, M, L, X, K, S, temp1, temp2, NULL);
}

int main() {
    mpf_t pi;
    mpf_init2(pi, PRECISION);

    chudnovsky_pi(pi);

    gmp_printf("Pi: %.Ff\n", pi);

    mpf_clear(pi);
    return 0;
}    