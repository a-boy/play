#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 9
#define EMPTY 0

int grid[N][N];

// 检查数字是否可以放在给定位置
int isSafe(int row, int col, int num) {
    // 检查行
    for (int x = 0; x < N; x++)
        if (grid[row][x] == num)
            return 0;
    
    // 检查列
    for (int x = 0; x < N; x++)
        if (grid[x][col] == num)
            return 0;
    
    // 检查3x3方格
    int startRow = row - row % 3, startCol = col - col % 3;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (grid[i + startRow][j + startCol] == num)
                return 0;
    
    return 1;
}

// 使用回溯法解决数独
int solveSudoku() {
    int row, col;
    
    // 寻找空格
    int isEmpty = 1;
    for (row = 0; row < N && isEmpty; row++) {
        for (col = 0; col < N; col++) {
            if (grid[row][col] == EMPTY) {
                isEmpty = 0;
                break;
            }
        }
        if (!isEmpty)
            break;
    }
    
    // 如果没有空格,数独已解决
    if (isEmpty)
        return 1;
    
    // 尝试填数
    for (int num = 1; num <= 9; num++) {
        if (isSafe(row, col, num)) {
            grid[row][col] = num;
            if (solveSudoku())
                return 1;
            grid[row][col] = EMPTY;
        }
    }
    
    return 0;
}

// 生成数独谜题
void generateSudoku() {
    // 初始化随机数生成器
    srand(time(NULL));
    
    // 清空网格
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            grid[i][j] = EMPTY;
    
    // 填充对角线上的3x3方格
    for (int i = 0; i < N; i += 3) {
        for (int num = 1; num <= 9; num++) {
            int row, col;
            do {
                row = i + rand() % 3;
                col = i + rand() % 3;
            } while (!isSafe(row, col, num));
            grid[row][col] = num;
        }
    }
    
    // 解决剩余的数独
    solveSudoku();
    
    // 移除一些数字以创建谜题
    int numToRemove = 40; // 可以调整难度
    while (numToRemove > 0) {
        int row = rand() % N;
        int col = rand() % N;
        if (grid[row][col] != EMPTY) {
            grid[row][col] = EMPTY;
            numToRemove--;
        }
    }
}

// 打印数独
void printSudoku() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%2d", grid[i][j]);
        printf("\n");
    }
}

int main() {
    generateSudoku();
    printf("生成的数独谜题:\n");
    printSudoku();
    
    printf("\n解决方案:\n");
    solveSudoku();
    printSudoku();
    
    return 0;
}

/* 这个程序包含以下主要功能:
generateSudoku(): 生成一个有效的数独谜题。
solveSudoku(): 使用回溯法解决数独。
3. isSafe(): 检查一个数字是否可以放在给定位置。
printSudoku(): 打印数独网格。
主函数 main() 首先生成一个数独谜题,然后打印出来,接着解决这个谜题并打印解决方案。
你可以编译并运行这个程序来生成和解决数独谜题。如果你想调整难度,可以在 generateSudoku() 函数中修改 numToRemove 的值。值越大,谜题越难。 */