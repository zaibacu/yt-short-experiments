#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define WIDTH 90
#define HEIGHT 30
#define DENSITY 10

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif


typedef enum { DEAD, ALIVE } state;

void print_grid(state grid[HEIGHT][WIDTH]){
    for(int y=0; y<HEIGHT; y++){
        for(int x=0; x<WIDTH; x++){
            if(grid[y][x] == DEAD){
                printf(" ");
            }
            else {
                printf("*");
            }
        }
        printf("\n");
    }
}

void init_grid(state grid[HEIGHT][WIDTH]){
    srand(time(0));
    for(int y=0; y<HEIGHT; y++){
        for(int x=0; x<WIDTH; x++){
            int g = rand() % 100;
            if(g <= DENSITY){
                grid[y][x] = ALIVE;
            }
            else {
                grid[y][x] = DEAD;
            }
        }
    }
}

void clear_screen(){
    #ifdef _WIN32
    system("cls");
    #else
    system("clear");
    #endif
}

void copy_data(state a[HEIGHT][WIDTH], state b[HEIGHT][WIDTH]){
    for(int y=0; y<HEIGHT; y++){
        for(int x=0; x<WIDTH; x++){
            b[y][x] = a[y][x];
        }
    }
}

int sum_alive(state grid[HEIGHT][WIDTH], int ox, int oy){
    int sum = 0;
    for(int dx=-1; dx<2; dx++){
        for(int dy=-1; dy<2; dy++){
            if(dy == 0 && dx == 0){
                continue;
            }
            int x = ox + dx;
            int y = oy + dy;

            if(x < 0){
                x = WIDTH - 1;
            }
            else if(x > (WIDTH - 1)){
                x = 0;
            }

            if(y < 0){
                y = HEIGHT - 1;
            }
            else if(y > (HEIGHT - 1)){
                y = 0;
            }

            if(grid[y][x] == ALIVE){
                sum++;
            }
        }
    }

    return sum;
}

void evolution(state orig_grid[HEIGHT][WIDTH]){
    state new_grid[HEIGHT][WIDTH];
    copy_data(orig_grid, new_grid);

    // Stuff
    for(int y=0; y<HEIGHT; y++){
        for(int x=0; x<WIDTH; x++){
            int n = sum_alive(orig_grid, x, y);
            if(orig_grid[y][x] == ALIVE){
                if(n < 2 || n > 3){
                    new_grid[y][x] = DEAD;
                }
            }
            else {
                if(n == 3){
                    new_grid[y][x] = ALIVE;
                }
            }
        }
    }

    copy_data(new_grid, orig_grid);
}


int main(int argc, char* argv[]){
    state grid[HEIGHT][WIDTH];
    init_grid(grid);

    while(1){
        clear_screen();
        print_grid(grid);
        sleep(1);
        evolution(grid);
    }
    return 0;
}