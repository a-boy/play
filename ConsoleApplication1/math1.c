#include <stdio.h>
#include <math.h>
#include <string.h>

int main(int argc, char **argv, char **envp){
        double x;
        char y[11];
        x=sqrt(argc+7.5);
        strncpy(y, argv[0], 10); /* prevent buffer overflow */
        y[10] = '\0'; /* fill to make sure string ends with '\0' */
        printf("%5i, %5.3f, %10s, %10s\n", argc, x, y, argv[1]);
        return 0;
}

// $ gcc -Wall -g -o math1 example.c -lm
// 为了使用 sqrt(3)，必须使用 “-lm” 链接来自 libc6 软件包的库 “/usr/lib/libm.so”。实际的库文件位于 “/lib/”，文件名为 “libm.so.6”，它是指向 “libm-2.7.so” 的一个链接。 