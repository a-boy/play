#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

// 迷宫结构
char maze[SIZE][SIZE];

// 初始化迷宫
void initMaze() {
    srand(time(NULL));
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (i == 0 || i == SIZE-1 || j == 0 || j == SIZE-1) {
                maze[i][j] = '#';
            } else {
                maze[i][j] = (rand() % 3 == 0) ? '#' : ' ';
            }
        }
    }
    maze[1][1] = 'S';
    maze[SIZE-2][SIZE-2] = 'E';
}

// 打印迷宫
void printMaze() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%c ", maze[i][j]);
        }
        printf("\n");
    }
}

// 深度优先搜索解决迷宫
int solveMaze(int x, int y) {
    if (x < 0 || x >= SIZE || y < 0 || y >= SIZE || maze[x][y] == '#') {
        return 0;
    }
    if (maze[x][y] == 'E') {
        return 1;
    }
    if (maze[x][y] == '.') {
        return 0;
    }
    maze[x][y] = '.';
    
    if (solveMaze(x+1, y) || solveMaze(x-1, y) || solveMaze(x, y+1) || solveMaze(x, y-1)) {
        return 1;
    }
    maze[x][y] = ' ';
    return 0;
}

int main() {
    initMaze();
    printf("生成的迷宫：\n");
    printMaze();
    
    if (solveMaze(1, 1)) {
        printf("\n解决后的迷宫：\n");
        printMaze();
    } else {
        printf("\n无法解决此迷宫。\n");
    }
    
    return 0;
}